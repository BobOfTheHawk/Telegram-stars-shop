from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List


def get_category_keyboard() -> InlineKeyboardMarkup:
    """Main category selection"""
    buttons = [
        [InlineKeyboardButton(text="💎 Telegram Premium", callback_data="category_premium")],
        [InlineKeyboardButton(text="⭐ Telegram Stars", callback_data="category_stars")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_premium_catalog_keyboard(products: List) -> InlineKeyboardMarkup:
    """Premium products keyboard"""
    buttons = []
    
    for product in products:
        price = f"{product.price_uzs:,}".replace(",", " ")
        emoji = "🔥" if product.duration_months >= 6 else "📦"
        
        button_text = f"{emoji} {product.duration_months} Month(s) - {price} UZS"
        buttons.append([
            InlineKeyboardButton(text=button_text, callback_data=f"product_{product.id}")
        ])
    
    buttons.append([
        InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_categories")
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_stars_catalog_keyboard(products: List) -> InlineKeyboardMarkup:
    """Stars products keyboard"""
    buttons = []
    
    for product in products:
        price = f"{product.price_uzs:,}".replace(",", " ")
        emoji = "🌟" if product.stars_amount >= 1000 else "⭐"
        
        button_text = f"{emoji} {product.stars_amount} Stars - {price} UZS"
        buttons.append([
            InlineKeyboardButton(text=button_text, callback_data=f"product_{product.id}")
        ])
    
    buttons.append([
        InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_categories")
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_product_detail_keyboard(product_id: int, product_type: str) -> InlineKeyboardMarkup:
    """Product detail view keyboard"""
    back_callback = "back_to_premium" if product_type == "premium" else "back_to_stars"
    
    buttons = [
        [InlineKeyboardButton(text="💳 Buy Now", callback_data=f"buy_{product_id}")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=back_callback)],
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_payment_confirmation_keyboard(product_id: int) -> InlineKeyboardMarkup:
    """Payment confirmation keyboard"""
    buttons = [
        [InlineKeyboardButton(text="✅ Confirm Purchase", callback_data=f"confirm_payment_{product_id}")],
        [InlineKeyboardButton(text="❌ Cancel", callback_data="back_to_categories")],
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_admin_menu_keyboard() -> InlineKeyboardMarkup:
    """Admin panel main menu"""
    buttons = [
        [InlineKeyboardButton(text="👥 Users", callback_data="admin_users")],
        [InlineKeyboardButton(text="💰 Revenue", callback_data="admin_revenue")],
        [InlineKeyboardButton(text="👑 Manage Admins", callback_data="admin_manage")],
        [InlineKeyboardButton(text="❌ Close", callback_data="close_admin")],
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)