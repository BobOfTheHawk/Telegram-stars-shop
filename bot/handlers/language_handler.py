from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.models import User

language_router = Router()


def get_language_keyboard() -> InlineKeyboardMarkup:
    """Language selection keyboard"""
    buttons = [
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="lang_uz")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@language_router.message(Command("language"))
@language_router.message(Command("lang"))
@language_router.message(F.text.contains("Language"))  # NEW
@language_router.message(F.text.contains("Язык"))      # NEW
@language_router.message(F.text.contains("Til"))       # NEW
async def show_language_menu(message: Message):
    """Show language selection menu"""
    
    user = await User.get(message.from_user.id)
    
    if user:
        current_lang = user.language or 'en'
        lang_names = {'en': '🇬🇧 English', 'ru': '🇷🇺 Русский', 'uz': '🇺🇿 O\'zbek'}
        current_name = lang_names.get(current_lang, '🇬🇧 English')
        
        text = (
            f"🌍 <b>Language / Язык / Til</b>\n\n"
            f"Current language: {current_name}\n"
            f"Текущий язык: {current_name}\n"
            f"Joriy til: {current_name}\n\n"
            f"Select your language:\n"
            f"Выберите язык:\n"
            f"Tilni tanlang:"
        )
    else:
        text = (
            "🌍 <b>Language / Язык / Til</b>\n\n"
            "Select your language:\n"
            "Выберите язык:\n"
            "Tilni tanlang:"
        )
    
    await message.answer(text, reply_markup=get_language_keyboard())


@language_router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    """Set user's language"""
    
    lang_code = callback.data.split("_")[1]
    
    user = await User.get(callback.from_user.id)
    
    if user:
        await User.update(user.id, language=lang_code)
        
        from bot.buttons.reply import main_menu
        
        success_messages = {
            'en': '✅ Language changed to English!',
            'ru': '✅ Язык изменен на Русский!',
            'uz': '✅ Til O\'zbek tiliga o\'zgartirildi!'
        }
        
        await callback.message.delete()
        await callback.message.answer(
            success_messages.get(lang_code, success_messages['en']),
            reply_markup=main_menu(lang_code)
        )
    else:
        await callback.message.edit_text(
            "❌ Please use /start first to register."
        )
    
    await callback.answer()