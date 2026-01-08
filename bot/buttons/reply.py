from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu(lang='en') -> ReplyKeyboardMarkup:
    """Main menu keyboard with language support"""
    
    # Button texts for each language
    buy_texts = {'en': '🛒 Buy Premium', 'ru': '🛒 Купить Премиум', 'uz': '🛒 Premium Sotib Olish'}
    profile_texts = {'en': '👤 My Profile', 'ru': '👤 Мой Профиль', 'uz': '👤 Mening Profilim'}
    help_texts = {'en': '❓ Help', 'ru': '❓ Помощь', 'uz': '❓ Yordam'}
    lang_texts = {'en': '🌍 Language', 'ru': '🌍 Язык', 'uz': '🌍 Til'}
    
    buttons = [
        [KeyboardButton(text=buy_texts.get(lang, buy_texts['en']))],
        [
            KeyboardButton(text=profile_texts.get(lang, profile_texts['en'])),
            KeyboardButton(text=help_texts.get(lang, help_texts['en']))
        ],
        [KeyboardButton(text=lang_texts.get(lang, lang_texts['en']))],  # Language button
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Choose an option..."
    )