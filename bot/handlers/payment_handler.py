from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, PreCheckoutQuery, LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from datetime import datetime, timedelta
from bot.buttons.inline import get_payment_confirmation_keyboard
from bot.state import PurchaseStates
from db.models import User, Product, Order, Transaction, GiftCode
from bot.dispacher import TOKEN
from aiogram import Bot
from utils.admin import get_all_admins
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

payment_router = Router()


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def get_unused_gift_code(duration_months: int):
    """Get an unused gift code for the specified duration"""
    codes = await GiftCode.get_all()
    unused_codes = [c for c in codes if not c.is_used and c.duration_months == duration_months]
    
    if unused_codes:
        return unused_codes[0]
    return None


@payment_router.callback_query(F.data.startswith("buy_"))
async def initiate_purchase(callback: CallbackQuery, state: FSMContext):
    """User clicked 'Buy Now' - show confirmation"""
    
    product_id = int(callback.data.split("_")[1])
    product = await Product.get(product_id)
    
    if not product or not product.is_active:
        await callback.answer("❌ This product is no longer available", show_alert=True)
        return
    
    await state.update_data(product_id=product_id)
    
    price_formatted = f"{product.price_uzs:,}".replace(",", " ")
    
    text = f"💳 <b>Purchase Confirmation</b>\n\n"
    text += f"📦 Product: {product.name}\n"
    text += f"💰 Price: {price_formatted} UZS\n"
    
    if product.product_type == 'premium':
        text += f"📅 Duration: {product.duration_months} month(s)\n"
    elif product.product_type == 'stars':
        text += f"⭐ Amount: {product.stars_amount} Stars\n"
    
    text += f"\n✅ Click 'Confirm Purchase' to proceed with payment."
    
    await callback.message.edit_text(
        text,
        reply_markup=get_payment_confirmation_keyboard(product_id)
    )
    await callback.answer()


@payment_router.callback_query(F.data.startswith("confirm_payment_"))
async def send_invoice(callback: CallbackQuery, state: FSMContext):
    """Send Telegram payment invoice"""
    
    product_id = int(callback.data.split("_")[2])
    product = await Product.get(product_id)
    
    if not product or not product.is_active:
        await callback.answer("❌ Product not available", show_alert=True)
        return
    
    user = await User.get(callback.from_user.id)
    
    # Create pending order
    order = await Order.create(
        user_id=user.id,
        product_id=product.id,
        amount=product.price_uzs,
        status='pending'
    )
    
    await state.update_data(order_id=order.id)
    
    from utils.config import CF
    
    try:
        await callback.message.answer_invoice(
            title=product.name,
            description=product.description or f"Purchase {product.name}",
            payload=f"order_{order.id}",
            provider_token=CF.pay.PAY_APP,
            currency="UZS",
            prices=[
                LabeledPrice(
                    label=product.name,
                    amount=product.price_uzs * 100
                )
            ],
            start_parameter=f"product_{product_id}",
            max_tip_amount=0,
            suggested_tip_amounts=[],
        )
        
        await callback.message.answer(
            "💳 <b>Invoice sent!</b>\n\n"
            "Click the 'Pay' button to complete your purchase."
        )
        
        await callback.answer()
        
    except Exception as e:
        print(f"Error sending invoice: {e}")
        await callback.message.answer("❌ Error sending invoice. Please try again.")
        await Order.update(order.id, status='cancelled')
        await callback.answer()


@payment_router.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    """Validate payment before processing"""
    
    try:
        payload = pre_checkout_query.invoice_payload
        
        if not payload.startswith("order_"):
            await pre_checkout_query.answer(ok=False, error_message="Invalid order")
            return
        
        order_id = int(payload.split("_")[1])
        order = await Order.get(order_id)
        
        if not order:
            await pre_checkout_query.answer(ok=False, error_message="Order not found")
            return
        
        if order.status != 'pending':
            await pre_checkout_query.answer(ok=False, error_message="Order already processed")
            return
        
        product = await Product.get(order.product_id)
        if not product or not product.is_active:
            await pre_checkout_query.answer(ok=False, error_message="Product not available")
            return
        
        expected_amount = product.price_uzs * 100
        if pre_checkout_query.total_amount != expected_amount:
            await pre_checkout_query.answer(ok=False, error_message="Price mismatch")
            return
        
        await pre_checkout_query.answer(ok=True)
        
    except Exception as e:
        print(f"Pre-checkout error: {e}")
        await pre_checkout_query.answer(ok=False, error_message="Validation failed")


@payment_router.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    """Handle successful payment"""
    
    try:
        payment_info = message.successful_payment
        payload = payment_info.invoice_payload
        order_id = int(payload.split("_")[1])
        
        order = await Order.get(order_id)
        if not order:
            await message.answer("❌ Error: Order not found")
            return
        
        user = await User.get(order.user_id)
        product = await Product.get(order.product_id)
        
        if not user or not product:
            await message.answer("❌ Error processing order")
            return
        
        # Update order with payment info
        await Order.update(
            order.id,
            status='paid',
            payment_charge_id=payment_info.telegram_payment_charge_id,
            telegram_payment_charge_id=payment_info.telegram_payment_charge_id,
            provider_payment_charge_id=payment_info.provider_payment_charge_id,
            paid_at=datetime.utcnow()
        )
        
        # Update user stats
        await User.update(
            user.id,
            total_spent=user.total_spent + product.price_uzs
        )
        
        # Increment product sales
        await Product.update(
            product.id,
            sales_count=product.sales_count + 1
        )
        
        # Create transaction
        await Transaction.create(
            user_id=user.id,
            order_id=order.id,
            amount=product.price_uzs,
            transaction_type='purchase',
            description=f"Purchased {product.name}"
        )
        
        # Handle based on product type
        if product.product_type == 'premium':
            # AUTOMATED: Premium with gift codes
            gift_code = await get_unused_gift_code(product.duration_months)
            
            if gift_code:
                # Mark code as used
                await GiftCode.update(
                    gift_code.id,
                    is_used=True,
                    used_by=user.id,
                    used_at=datetime.utcnow(),
                    order_id=order.id
                )
                
                # Mark order complete
                await Order.update(
                    order.id,
                    status='completed',
                    completed_at=datetime.utcnow()
                )
                
                # Send gift code to user
                await message.answer(
                    f"🎉 <b>Payment Successful!</b>\n\n"
                    f"✅ Your Premium Gift Code:\n\n"
                    f"<code>{gift_code.code}</code>\n\n"
                    f"📱 <b>How to redeem:</b>\n"
                    f"1. Tap on the code to copy it\n"
                    f"2. Open Telegram Settings\n"
                    f"3. Tap 'Telegram Premium'\n"
                    f"4. Tap 'Have a gift code?'\n"
                    f"5. Paste and activate\n\n"
                    f"💎 Enjoy your {product.duration_months} month(s) of Premium!"
                )
                
                # Notify admins
                admins = await get_all_admins()
                for admin in admins:
                    try:
                        await bot.send_message(
                            admin.user_id,
                            f"💰 <b>Premium Sale (Automated)</b>\n\n"
                            f"👤 User: {user.fullname} (@{user.username or 'N/A'})\n"
                            f"🆔 User ID: {user.id}\n"
                            f"📦 Product: {product.name}\n"
                            f"💵 Amount: {payment_info.total_amount // 100:,} UZS\n"
                            f"🆔 Order: #{order.id}\n"
                            f"✅ Status: Completed (Gift code sent)"
                        )
                    except:
                        pass
            
            else:
                # No gift codes available
                await Order.update(order.id, status='pending_fulfillment')
                
                await message.answer(
                    f"✅ Payment confirmed: {payment_info.total_amount // 100:,} UZS\n\n"
                    f"⚠️ Gift codes are currently out of stock.\n"
                    f"Our admin will send your Premium code within a few minutes.\n\n"
                    f"Order ID: #{order.id}"
                )
                
                # Urgent admin notification
                admins = await get_all_admins()
                for admin in admins:
                    try:
                        await bot.send_message(
                            admin.user_id,
                            f"🚨 <b>URGENT - No Gift Codes!</b>\n\n"
                            f"Order #{order.id} needs manual Premium code.\n"
                            f"User: {user.fullname} (@{user.username or 'N/A'})\n"
                            f"Duration: {product.duration_months} months\n"
                            f"User ID: <code>{user.id}</code>\n\n"
                            f"Action: /addcode {product.duration_months} <code>"
                        )
                    except:
                        pass
        
        elif product.product_type == 'stars':
            # MANUAL: Stars fulfillment
            await Order.update(order.id, status='pending_fulfillment')
            
            await message.answer(
                f"✅ <b>Payment Confirmed!</b>\n\n"
                f"💰 Amount: {payment_info.total_amount // 100:,} UZS\n"
                f"⭐ You will receive: {product.stars_amount} Stars\n\n"
                f"⏳ Processing... You'll receive your Stars within 1-2 minutes!\n\n"
                f"Order ID: #{order.id}"
            )
            
            # Notify admins with quick action button
            admins = await get_all_admins()
            for admin in admins:
                try:
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(
                            text="✅ Mark as Completed",
                            callback_data=f"complete_order_{order.id}"
                        )]
                    ])
                    
                    await bot.send_message(
                        admin.user_id,
                        f"🚨 <b>URGENT - STARS ORDER</b>\n\n"
                        f"👤 User: {user.fullname}\n"
                        f"📱 Username: @{user.username or 'N/A'}\n"
                        f"🆔 User ID: <code>{user.id}</code>\n\n"
                        f"⭐ Amount: <b>{product.stars_amount} Stars</b>\n"
                        f"💵 Paid: {payment_info.total_amount // 100:,} UZS\n"
                        f"🆔 Order: #{order.id}\n\n"
                        f"📱 <b>ACTION:</b> Send {product.stars_amount} Stars to:\n"
                        f"User ID: <code>{user.id}</code>\n\n"
                        f"Then click the button below ⬇️",
                        reply_markup=keyboard
                    )
                except Exception as e:
                    print(f"Failed to notify admin {admin.user_id}: {e}")
        
    except Exception as e:
        print(f"Error processing payment: {e}")
        await message.answer("⚠️ Payment received but there was an error. Please contact support.")


@payment_router.callback_query(F.data.startswith("complete_order_"))
async def quick_complete_order(callback: CallbackQuery):
    """Admin marks order as completed"""
    from bot.filters import IsAdminCallback
    
    # Check if admin
    if not await IsAdminCallback()(callback):
        await callback.answer("❌ Admin only", show_alert=True)
        return
    
    order_id = int(callback.data.split("_")[-1])
    
    order = await Order.get(order_id)
    if not order:
        await callback.answer("❌ Order not found", show_alert=True)
        return
    
    await Order.update(
        order_id,
        status='completed',
        completed_at=datetime.utcnow()
    )
    
    user = await User.get(order.user_id)
    product = await Product.get(order.product_id)
    
    # Notify user
    try:
        await bot.send_message(
            user.id,
            f"✅ <b>Stars Delivered!</b>\n\n"
            f"⭐ You have received {product.stars_amount} Stars\n\n"
            f"Thank you for your purchase! 💫"
        )
    except:
        pass
    
    await callback.message.edit_text(
        f"✅ <b>Order #{order_id} Completed!</b>\n\n"
        f"User has been notified.\n"
        f"Stars: {product.stars_amount}\n"
        f"User: {user.fullname} (@{user.username or 'N/A'})"
    )
    await callback.answer("✅ Order completed!")