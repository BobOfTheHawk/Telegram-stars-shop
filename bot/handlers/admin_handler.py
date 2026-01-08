from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from bot.filters import IsAdmin, IsAdminCallback
from bot.buttons.inline import get_admin_menu_keyboard
from utils.admin import get_all_admins, add_admin, remove_admin, is_admin
from db.models import User, Product, Order, GiftCode
from datetime import datetime, timedelta
from bot.dispacher import TOKEN
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

admin_router = Router()


@admin_router.message(Command("admin"), IsAdmin())
async def admin_panel(message: Message):
    """Show admin panel"""
    
    users = await User.get_all()
    products = await Product.get_all()
    orders = await Order.get_all()
    
    total_users = len(users)
    premium_users = len([u for u in users if u.is_premium and u.premium_until and u.premium_until > datetime.utcnow()])
    total_revenue = sum([u.total_spent for u in users])
    completed_orders = len([o for o in orders if o.status == 'completed'])
    
    text = "🔐 <b>Admin Panel</b>\n\n"
    text += f"👥 Total Users: {total_users}\n"
    text += f"💎 Premium Users: {premium_users}\n"
    text += f"💰 Total Revenue: {total_revenue:,} UZS\n"
    text += f"📦 Completed Orders: {completed_orders}\n\n"
    text += "Choose an option:"
    
    await message.answer(text, reply_markup=get_admin_menu_keyboard())


@admin_router.callback_query(F.data == "admin_users", IsAdminCallback())
async def show_admin_users(callback: CallbackQuery):
    """Show recent users"""
    
    users = await User.get_all()
    recent_users = sorted(users, key=lambda x: x.created_at, reverse=True)[:10]
    
    text = "👥 <b>Recent Users</b>\n\n"
    
    for user in recent_users:
        status = "💎" if user.is_premium else "👤"
        text += f"{status} {user.fullname} (@{user.username or 'N/A'})\n"
        text += f"   ID: {user.id} | Spent: {user.total_spent:,} UZS\n\n"
    
    await callback.message.edit_text(text, reply_markup=get_admin_menu_keyboard())
    await callback.answer()


@admin_router.callback_query(F.data == "admin_revenue", IsAdminCallback())
async def show_revenue(callback: CallbackQuery):
    """Show revenue statistics"""
    
    orders = await Order.get_all()
    completed = [o for o in orders if o.status == 'completed']
    
    total_revenue = sum([o.amount for o in completed])
    
    today = datetime.utcnow().date()
    today_orders = [o for o in completed if o.completed_at and o.completed_at.date() == today]
    today_revenue = sum([o.amount for o in today_orders])
    
    this_month = datetime.utcnow().replace(day=1)
    month_orders = [o for o in completed if o.completed_at and o.completed_at >= this_month]
    month_revenue = sum([o.amount for o in month_orders])
    
    text = "💰 <b>Revenue Statistics</b>\n\n"
    text += f"📊 Total Revenue: {total_revenue:,} UZS\n"
    text += f"📅 Today: {today_revenue:,} UZS ({len(today_orders)} orders)\n"
    text += f"📆 This Month: {month_revenue:,} UZS ({len(month_orders)} orders)\n\n"
    text += f"Total Orders: {len(completed)}"
    
    await callback.message.edit_text(text, reply_markup=get_admin_menu_keyboard())
    await callback.answer()


@admin_router.callback_query(F.data == "admin_manage", IsAdminCallback())
async def manage_admins(callback: CallbackQuery):
    """Show admin management"""
    
    admins = await get_all_admins()
    
    text = "👑 <b>Admin Management</b>\n\n"
    text += f"Total Admins: {len(admins)}\n\n"
    
    for admin in admins:
        text += f"• {admin.fullname or 'Unknown'} (@{admin.username or 'N/A'})\n"
        text += f"  ID: {admin.user_id}\n"
        text += f"  Added: {admin.created_at.strftime('%Y-%m-%d')}\n\n"
    
    text += "\nTo add admin: /addadmin (user_id)\n"
    text += "To remove admin: /removeadmin (user_id)"
    
    with contextlib.suppress(TelegramBadRequest):
            await callback.message.edit_text(
                text, 
                reply_markup=get_admin_menu_keyboard()
            )
    
    # await callback.message.edit_text(text, reply_markup=get_admin_menu_keyboard())
    # await callback.answer()


@admin_router.message(Command("addadmin"), IsAdmin())
async def add_admin_command(message: Message):
    """Add a new admin"""
    
    args = message.text.split()
    
    if len(args) != 2:
        await message.answer(
            "❌ Usage: /addadmin (user_id)\n\n"
            "Example: /addadmin 123456789"
        )
        return
    
    try:
        new_admin_id = int(args[1])
    except ValueError:
        await message.answer("❌ Invalid user ID. Must be a number.")
        return
    
    if await is_admin(new_admin_id):
        await message.answer("ℹ️ This user is already an admin.")
        return
    
    user = await User.get(new_admin_id)
    
    if user:
        username = user.username
        fullname = user.fullname
    else:
        username = None
        fullname = f"User {new_admin_id}"
    
    await add_admin(
        user_id=new_admin_id,
        username=username,
        fullname=fullname,
        added_by=message.from_user.id
    )
    
    await message.answer(
        f"✅ Admin added successfully!\n\n"
        f"User: {fullname}\n"
        f"ID: {new_admin_id}"
    )


@admin_router.message(Command("removeadmin"), IsAdmin())
async def remove_admin_command(message: Message):
    """Remove an admin"""
    
    args = message.text.split()
    
    if len(args) != 2:
        await message.answer(
            "❌ Usage: /removeadmin (user_id)\n\n"
            "Example: /removeadmin 123456789"
        )
        return
    
    try:
        admin_id = int(args[1])
    except ValueError:
        await message.answer("❌ Invalid user ID. Must be a number.")
        return
    
    if admin_id == message.from_user.id:
        await message.answer("❌ You cannot remove yourself as admin.")
        return
    
    if not await is_admin(admin_id):
        await message.answer("ℹ️ This user is not an admin.")
        return
    
    success = await remove_admin(admin_id)
    
    if success:
        await message.answer(f"✅ Admin removed: {admin_id}")
    else:
        await message.answer("❌ Failed to remove admin.")


@admin_router.message(Command("admins"), IsAdmin())
async def list_admins(message: Message):
    """List all admins"""
    
    admins = await get_all_admins()
    
    text = "👑 <b>Admin List</b>\n\n"
    
    for admin in admins:
        text += f"• {admin.fullname or 'Unknown'}\n"
        text += f"  @{admin.username or 'N/A'} | ID: {admin.user_id}\n"
        text += f"  Added: {admin.created_at.strftime('%Y-%m-%d')}\n\n"
    
    await message.answer(text)


@admin_router.message(Command("addcode"), IsAdmin())
async def add_gift_code(message: Message):
    """Add a new gift code"""
    
    args = message.text.split(maxsplit=2)
    
    if len(args) != 3:
        await message.answer(
            "❌ Usage: /addcode (months) (code)\n\n"
            "Example:\n"
            "/addcode 1 t.me/giftcode/abc123xyz\n"
            "/addcode 3 PREMIUM-CODE-HERE"
        )
        return
    
    try:
        months = int(args[1])
        code = args[2]
        
        gift_code = await GiftCode.create(
            code=code,
            duration_months=months,
            is_used=False
        )
        
        await message.answer(
            f"✅ Gift code added!\n\n"
            f"Duration: {months} month(s)\n"
            f"Code: {code}"
        )
        
    except Exception as e:
        await message.answer(f"❌ Error: {e}")


@admin_router.message(Command("codes"), IsAdmin())
async def list_gift_codes(message: Message):
    """List gift code inventory"""
    
    codes = await GiftCode.get_all()
    
    if not codes:
        await message.answer("📭 No gift codes in system.")
        return
    
    unused_codes = [c for c in codes if not c.is_used]
    
    text = "🎁 <b>Gift Code Inventory</b>\n\n"
    
    for months in [1, 3, 6, 12]:
        count = len([c for c in unused_codes if c.duration_months == months])
        emoji = "🔴" if count < 5 else "🟡" if count < 10 else "🟢"
        text += f"{emoji} {months} month(s): {count} available\n"
    
    text += f"\n📊 Total unused: {len(unused_codes)}"
    
    await message.answer(text)


@admin_router.message(Command("complete"), IsAdmin())
async def manual_complete_order(message: Message):
    """Manually complete an order"""
    
    args = message.text.split()
    
    if len(args) != 2:
        await message.answer("❌ Usage: /complete (order_id)")
        return
    
    try:
        order_id = int(args[1])
        
        order = await Order.get(order_id)
        if not order:
            await message.answer("❌ Order not found")
            return
        
        await Order.update(
            order_id,
            status='completed',
            completed_at=datetime.utcnow()
        )
        
        user = await User.get(order.user_id)
        product = await Product.get(order.product_id)
        
        bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        
        await bot.send_message(
            user.id,
            "✅ Your order is complete!\n\n"
            "Thank you for your purchase! 💎"
        )
        
        await message.answer(
            f"✅ Order #{order_id} completed!\n"
            f"User: {user.fullname}\n"
            f"Product: {product.name}"
        )
        
    except Exception as e:
        await message.answer(f"❌ Error: {e}")


@admin_router.message(Command("products"), IsAdmin())
async def list_products(message: Message):
    """List all products with IDs and prices"""
    
    products = await Product.get_all()
    
    if not products:
        await message.answer("📭 No products in system.")
        return
    
    premium_products = sorted([p for p in products if p.product_type == 'premium'], key=lambda x: x.duration_months or 0)
    stars_products = sorted([p for p in products if p.product_type == 'stars'], key=lambda x: x.stars_amount or 0)
    
    text = "📦 <b>Products and Pricing</b>\n\n"
    
    if premium_products:
        text += "💎 <b>Premium Packages:</b>\n\n"
        for p in premium_products:
            status = "✅" if p.is_active else "❌"
            price = f"{p.price_uzs:,}".replace(",", " ")
            text += f"{status} ID: <b>{p.id}</b> | {p.duration_months}mo | {price} UZS\n"
            text += f"   Sales: {p.sales_count}\n\n"
    
    if stars_products:
        text += "⭐ <b>Stars Packages:</b>\n\n"
        for p in stars_products:
            status = "✅" if p.is_active else "❌"
            price = f"{p.price_uzs:,}".replace(",", " ")
            text += f"{status} ID: <b>{p.id}</b> | {p.stars_amount}★ | {price} UZS\n"
            text += f"   Sales: {p.sales_count}\n\n"
    
    text += "\n💡 Use /setprice (id) (price) to change prices"
    
    await message.answer(text)


@admin_router.message(Command("setprice"), IsAdmin())
async def set_product_price(message: Message):
    """Change product price"""
    
    args = message.text.split()
    
    if len(args) != 3:
        products = await Product.get_all()
        text = "❌ Usage: /setprice (product_id) (new_price)\n\n"
        text += "Example: /setprice 5 70000\n\n"
        text += "<b>Available Products:</b>\n"
        for p in products:
            text += f"• ID: {p.id} - {p.name}\n"
        await message.answer(text)
        return
    
    try:
        product_id = int(args[1])
        new_price = int(args[2])
        
        product = await Product.get(product_id)
        if not product:
            products = await Product.get_all()
            text = f"❌ Product ID {product_id} not found!\n\n"
            text += "<b>Available Products:</b>\n"
            for p in products:
                text += f"• ID: {p.id} - {p.name}\n"
            await message.answer(text)
            return
        
        old_price = product.price_uzs
        
        await Product.update(
            product_id,
            price_uzs=new_price
        )
        
        await message.answer(
            f"✅ Price updated!\n\n"
            f"Product: {product.name}\n"
            f"Old Price: {old_price:,} UZS\n"
            f"New Price: {new_price:,} UZS"
        )
        
    except ValueError:
        await message.answer("❌ Invalid numbers. Use integers only.\nExample: /setprice 5 70000")
    except Exception as e:
        await message.answer(f"❌ Error: {e}")


@admin_router.message(Command("toggle"), IsAdmin())
async def toggle_product(message: Message):
    """Enable or disable product"""
    
    args = message.text.split()
    
    if len(args) != 2:
        products = await Product.get_all()
        text = "❌ Usage: /toggle (product_id)\n\n"
        text += "Example: /toggle 5\n\n"
        text += "<b>Available Products:</b>\n"
        for p in products:
            status = "✅" if p.is_active else "❌"
            text += f"{status} ID: {p.id} - {p.name}\n"
        await message.answer(text)
        return
    
    try:
        product_id = int(args[1])
        
        product = await Product.get(product_id)
        if not product:
            products = await Product.get_all()
            text = f"❌ Product ID {product_id} not found!\n\n"
            text += "<b>Available Products:</b>\n"
            for p in products:
                status = "✅" if p.is_active else "❌"
                text += f"{status} ID: {p.id} - {p.name}\n"
            await message.answer(text)
            return
        
        new_status = not product.is_active
        
        await Product.update(
            product_id,
            is_active=new_status
        )
        
        status_text = "Enabled ✅" if new_status else "Disabled ❌"
        
        await message.answer(
            f"{status_text}\n\n"
            f"Product: {product.name}\n"
            f"Status: {'Active' if new_status else 'Inactive'}"
        )
        
    except ValueError:
        await message.answer("❌ Invalid product ID. Use a number.\nExample: /toggle 5")
    except Exception as e:
        await message.answer(f"❌ Error: {e}")
