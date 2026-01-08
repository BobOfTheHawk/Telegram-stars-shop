from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from bot.buttons.inline import (
    get_category_keyboard,
    get_premium_catalog_keyboard,
    get_stars_catalog_keyboard,
    get_product_detail_keyboard
)
from db.models import Product, User
from utils.i18n import get_text

catalog_router = Router()


@catalog_router.message(Command("catalog"))
@catalog_router.message(F.text.contains("Buy Premium"))
@catalog_router.message(F.text.contains("Sotib Olish"))
@catalog_router.message(F.text.contains("Купить"))
async def show_categories(message: Message):
    """Show category selection: Premium or Stars"""
    
    user = await User.get(message.from_user.id)
    lang = user.language if user else 'en'
    
    text = (
        get_text(lang, 'store_welcome') + '\n\n' +
        get_text(lang, 'store_subtitle') + '\n\n' +
        get_text(lang, 'category_premium_title') + '\n' +
        get_text(lang, 'category_premium_desc') + '\n\n' +
        get_text(lang, 'category_stars_title') + '\n' +
        get_text(lang, 'category_stars_desc') + '\n\n' +
        get_text(lang, 'choose_category')
    )
    
    await message.answer(text, reply_markup=get_category_keyboard())


@catalog_router.callback_query(F.data == "category_premium")
async def show_premium_catalog(callback: CallbackQuery):
    """Show Premium packages"""
    
    user = await User.get(callback.from_user.id)
    lang = user.language if user else 'en'
    
    products = await Product.get_all()
    premium_products = sorted(
        [p for p in products if p.product_type == 'premium' and p.is_active],
        key=lambda x: x.duration_months
    )
    
    if not premium_products:
        await callback.answer(get_text(lang, 'error_not_available'), show_alert=True)
        return
    
    text = (
        get_text(lang, 'premium_title') + '\n\n' +
        get_text(lang, 'premium_features') + '\n' +
        get_text(lang, 'feature_downloads') + '\n' +
        get_text(lang, 'feature_stickers') + '\n' +
        get_text(lang, 'feature_voice') + '\n' +
        get_text(lang, 'feature_no_ads') + '\n' +
        get_text(lang, 'feature_icon') + '\n' +
        get_text(lang, 'feature_channels') + '\n\n'
    )
    
    one_month = next((p for p in premium_products if p.duration_months == 1), None)
    
    for product in premium_products:
        price_formatted = f"{product.price_uzs:,}".replace(",", " ")
        price_per_month = product.price_uzs // product.duration_months
        price_per_month_formatted = f"{price_per_month:,}".replace(",", " ")
        
        discount_text = ""
        if one_month and product.duration_months > 1:
            regular = one_month.price_uzs * product.duration_months
            savings = regular - product.price_uzs
            if savings > 0:
                discount_percent = (savings / regular) * 100
                discount_text = " " + get_text(lang, 'save_percent', percent=f"{discount_percent:.0f}")
        
        emoji = "🔥" if product.duration_months >= 6 else "📦"
        
        text += f"{emoji} <b>{product.duration_months} Month(s)</b>{discount_text}\n"
        text += f"   💰 {price_formatted} UZS\n"
        text += f"   📊 {get_text(lang, 'per_month', price=price_per_month_formatted)}\n\n"
    
    text += get_text(lang, 'select_package')
    
    await callback.message.edit_text(
        text,
        reply_markup=get_premium_catalog_keyboard(premium_products)
    )
    await callback.answer()


@catalog_router.callback_query(F.data == "category_stars")
async def show_stars_catalog(callback: CallbackQuery):
    """Show Stars packages"""
    
    products = await Product.get_all()
    stars_products = sorted(
        [p for p in products if p.product_type == 'stars' and p.is_active],
        key=lambda x: x.stars_amount
    )
    
    if not stars_products:
        await callback.answer("❌ No Stars packages available", show_alert=True)
        return
    
    text = (
        "⭐ <b>Telegram Stars</b>\n\n"
        "Use Stars to:\n"
        "• 🎁 Send gifts to others\n"
        "• 💬 Support content creators\n"
        "• 🎨 Buy premium stickers\n"
        "• 🎮 Purchase in-app items\n\n"
    )
    
    for product in stars_products:
        price_formatted = f"{product.price_uzs:,}".replace(",", " ")
        
        # Calculate price per star
        price_per_star = product.price_uzs / product.stars_amount
        
        emoji = "🌟" if product.stars_amount >= 1000 else "⭐"
        
        text += f"{emoji} <b>{product.stars_amount} Stars</b>\n"
        text += f"   💰 {price_formatted} UZS\n"
        text += f"   📊 ~{price_per_star:.1f} UZS per star\n\n"
    
    text += "👇 Select a package:"
    
    await callback.message.edit_text(
        text,
        reply_markup=get_stars_catalog_keyboard(stars_products)
    )
    await callback.answer()


@catalog_router.callback_query(F.data.startswith("product_"))
async def show_product_detail(callback: CallbackQuery):
    """Show detailed information about a selected product"""
    
    product_id = int(callback.data.split("_")[1])
    product = await Product.get(product_id)
    
    if not product or not product.is_active:
        await callback.answer("❌ This product is no longer available", show_alert=True)
        return
    
    price_formatted = f"{product.price_uzs:,}".replace(",", " ")
    
    text = f"{'💎' if product.product_type == 'premium' else '⭐'} <b>{product.name}</b>\n\n"
    
    if product.product_type == 'premium' and product.duration_months:
        text += f"📅 <b>Duration:</b> {product.duration_months} month(s)\n"
        text += f"💰 <b>Price:</b> {price_formatted} UZS\n"
        
        price_per_month = product.price_uzs // product.duration_months
        text += f"📊 <b>Per month:</b> {price_per_month:,} UZS\n\n"
        
        # Calculate savings
        if product.duration_months > 1:
            products = await Product.get_all()
            one_month = next((p for p in products if p.product_type == 'premium' and p.duration_months == 1), None)
            if one_month:
                regular = one_month.price_uzs * product.duration_months
                savings = regular - product.price_uzs
                if savings > 0:
                    discount_percent = (savings / regular) * 100
                    savings_formatted = f"{savings:,}".replace(",", " ")
                    text += f"🎉 <b>You save:</b> {savings_formatted} UZS ({discount_percent:.0f}% off!)\n\n"
        
        text += "✨ <b>Premium Features:</b>\n"
        text += "• ⚡ Faster downloads (up to 4GB)\n"
        text += "• 🎨 Exclusive stickers & reactions\n"
        text += "• 🎙️ Voice-to-text conversion\n"
        text += "• 🚫 No ads\n"
        text += "• 📱 Premium app icon\n"
        text += "• 📢 Unlimited channels & folders\n"
        text += "• 👁️ Read receipts\n"
        text += "• And much more!\n\n"
    
    elif product.product_type == 'stars' and product.stars_amount:
        text += f"⭐ <b>Amount:</b> {product.stars_amount} Stars\n"
        text += f"💰 <b>Price:</b> {price_formatted} UZS\n\n"
        
        price_per_star = product.price_uzs / product.stars_amount
        text += f"📊 ~{price_per_star:.1f} UZS per star\n\n"
        
        text += "✨ <b>What are Stars?</b>\n"
        text += "• 🎁 Send premium gifts\n"
        text += "• 💬 Support content creators\n"
        text += "• 🎨 Buy exclusive stickers\n"
        text += "• 🎮 Purchase in-app items\n\n"
        text += "⚡ Delivered within 1-2 minutes!\n\n"
    
    text += "👇 Ready to purchase?"
    
    await callback.message.edit_text(
        text,
        reply_markup=get_product_detail_keyboard(product_id, product.product_type)
    )
    await callback.answer()


@catalog_router.callback_query(F.data == "back_to_categories")
async def back_to_categories(callback: CallbackQuery):
    """Go back to category selection"""
    
    text = (
        "💎 <b>Welcome to Our Store!</b>\n\n"
        "What would you like to purchase?\n\n"
        "🎁 <b>Telegram Premium</b>\n"
        "Unlock exclusive features and faster downloads\n\n"
        "⭐ <b>Telegram Stars</b>\n"
        "Buy digital goods and support creators\n\n"
        "👇 Choose a category below:"
    )
    
    await callback.message.edit_text(text, reply_markup=get_category_keyboard())
    await callback.answer()


@catalog_router.callback_query(F.data == "back_to_premium")
async def back_to_premium(callback: CallbackQuery):
    """Go back to premium catalog"""
    await show_premium_catalog(callback)


@catalog_router.callback_query(F.data == "back_to_stars")
async def back_to_stars(callback: CallbackQuery):
    """Go back to stars catalog"""
    await show_stars_catalog(callback)