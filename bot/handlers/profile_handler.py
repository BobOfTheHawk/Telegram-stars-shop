from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime
from db.models import User, Order
from utils.i18n import get_text

profile_router = Router()


@profile_router.message(Command("profile"))
@profile_router.message(F.text.contains("Profile"))
@profile_router.message(F.text.contains("Профиль"))
@profile_router.message(F.text.contains("Profil"))
async def show_profile(message: Message):
    """Show user's profile and premium status"""
    
    user = await User.get(message.from_user.id)
    
    if not user:
        await message.answer(get_text('en', 'error_user_not_found'))
        return
    
    lang = user.language or 'en'
    
    is_premium_active = False
    days_remaining = 0
    
    if user.is_premium and user.premium_until:
        if user.premium_until > datetime.utcnow():
            is_premium_active = True
            days_remaining = (user.premium_until - datetime.utcnow()).days
    
    text = get_text(lang, 'your_profile') + '\n\n'
    text += get_text(lang, 'name', name=user.fullname) + '\n'
    text += get_text(lang, 'user_id', id=user.id) + '\n'
    text += get_text(lang, 'username', username=user.username or 'Not set') + '\n'
    text += get_text(lang, 'member_since', date=user.created_at.strftime('%d %B %Y')) + '\n\n'
    
    if is_premium_active:
        text += get_text(lang, 'premium_active') + '\n'
        text += get_text(lang, 'expires', date=user.premium_until.strftime('%d %B %Y, %H:%M')) + '\n'
        text += get_text(lang, 'days_remaining', days=days_remaining) + '\n\n'
    else:
        text += get_text(lang, 'status_free_title') + '\n\n'
        text += get_text(lang, 'upgrade_prompt') + '\n\n'
    
    text += get_text(lang, 'your_stats') + '\n'
    text += get_text(lang, 'total_spent', amount=f"{user.total_spent:,}") + '\n'
    
    orders = await Order.get_all()
    user_orders = [o for o in orders if o.user_id == user.id]
    completed_orders = [o for o in user_orders if o.status == 'completed']
    
    text += get_text(lang, 'total_orders', count=len(completed_orders)) + '\n'
    
    if not is_premium_active:
        text += '\n' + get_text(lang, 'ready_upgrade')
    
    await message.answer(text)


@profile_router.message(Command("orders"))
async def show_orders(message: Message):
    """Show user's order history"""
    
    user = await User.get(message.from_user.id)
    
    if not user:
        await message.answer("❌ User not found. Please use /start to register.")
        return
    
    orders = await Order.get_all()
    user_orders = sorted(
        [o for o in orders if o.user_id == user.id],
        key=lambda x: x.created_at,
        reverse=True
    )
    
    if not user_orders:
        await message.answer(
            "📭 No orders yet.\n\n"
            "Start shopping by tapping 'Buy Premium' below!"
        )
        return
    
    text = f"📜 <b>Your Order History</b>\n\n"
    
    from db.models import Product
    
    for order in user_orders[:10]:  # Show last 10 orders
        product = await Product.get(order.product_id)
        product_name = product.name if product else "Unknown Product"
        
        status_emoji = {
            'completed': '✅',
            'pending': '⏳',
            'pending_fulfillment': '⏳',
            'cancelled': '❌',
            'refunded': '↩️'
        }.get(order.status, '❓')
        
        text += f"{status_emoji} <b>Order #{order.id}</b>\n"
        text += f"   {product_name}\n"
        text += f"   {order.amount:,} UZS | {order.status.title()}\n"
        text += f"   {order.created_at.strftime('%d %b %Y, %H:%M')}\n\n"
    
    if len(user_orders) > 10:
        text += f"... and {len(user_orders) - 10} more orders"
    
    await message.answer(text)