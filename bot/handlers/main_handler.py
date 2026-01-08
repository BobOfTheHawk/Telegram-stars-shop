from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.buttons.reply import main_menu
from bot.state import RegistrationStates
from db.models import User
from utils.i18n import get_text

main_router = Router()


def get_language_selection_keyboard() -> InlineKeyboardMarkup:
    """Language selection keyboard for registration"""
    buttons = [
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="register_lang_en")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="register_lang_ru")],
        [InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="register_lang_uz")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@main_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """Handle /start command"""
    user = await User.get(id_=message.from_user.id)
    await state.clear()
    
    if not user:
        # New user - ask for language first
        text = (
            "🌍 <b>Welcome! Choose your language:</b>\n"
            "Добро пожаловать! Выберите язык:\n"
            "Xush kelibsiz! Tilni tanlang:"
        )
        
        await message.answer(text, reply_markup=get_language_selection_keyboard())
        await state.set_state(RegistrationStates.waiting_for_language)
    else:
        # Existing user
        lang = user.language or 'en'
        status = get_text(lang, 'status_premium') if user.is_premium else get_text(lang, 'status_free')
        
        await message.answer(
            get_text(lang, 'welcome_back', name=user.fullname) + '\n\n' +
            get_text(lang, 'status', status=status) + '\n\n' +
            get_text(lang, 'choose_option'),
            reply_markup=main_menu(lang)
        )


@main_router.callback_query(F.data.startswith("register_lang_"))
async def process_language_selection(callback: CallbackQuery, state: FSMContext):
    """Process language selection during registration"""
    
    lang_code = callback.data.split("_")[-1]
    
    # Save language to state
    await state.update_data(language=lang_code)
    
    # Ask for fullname in selected language
    welcome_messages = {
        'en': "👋 Welcome to Premium Telegram Bot!\n\nPlease enter your full name:",
        'ru': "👋 Добро пожаловать в Premium Telegram Bot!\n\nПожалуйста, введите ваше полное имя:",
        'uz': "👋 Premium Telegram Botga xush kelibsiz!\n\nIltimos, to'liq ismingizni kiriting:"
    }
    
    await callback.message.edit_text(
        welcome_messages.get(lang_code, welcome_messages['en'])
    )
    
    await state.set_state(RegistrationStates.waiting_for_fullname)
    await callback.answer()


@main_router.message(RegistrationStates.waiting_for_fullname)
async def process_fullname(message: Message, state: FSMContext) -> None:
    """Save user's fullname and ask for phone number"""
    fullname = message.text.strip()
    
    data = await state.get_data()
    lang = data.get('language', 'en')
    
    if len(fullname) < 2:
        error_messages = {
            'en': "❌ Please enter a valid name (at least 2 characters):",
            'ru': "❌ Пожалуйста, введите корректное имя (минимум 2 символа):",
            'uz': "❌ Iltimos, to'g'ri ism kiriting (kamida 2 ta harf):"
        }
        await message.answer(error_messages.get(lang, error_messages['en']))
        return
    
    await state.update_data(fullname=fullname)
    
    phone_messages = {
        'en': f"✅ Great, {fullname}!\n\nNow please share your phone number:",
        'ru': f"✅ Отлично, {fullname}!\n\nТеперь поделитесь своим номером телефона:",
        'uz': f"✅ Ajoyib, {fullname}!\n\nEndi telefon raqamingizni ulashing:"
    }
    
    await message.answer(
        phone_messages.get(lang, phone_messages['en']),
        reply_markup=get_phone_keyboard(lang)
    )
    await state.set_state(RegistrationStates.waiting_for_phone)


@main_router.message(RegistrationStates.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext) -> None:
    """Save user's phone and complete registration"""
    
    if message.contact:
        phone_number = message.contact.phone_number
    else:
        phone_number = message.text.strip()
    
    data = await state.get_data()
    lang = data.get('language', 'en')
    
    if not phone_number or len(phone_number) < 9:
        error_messages = {
            'en': "❌ Please enter a valid phone number:",
            'ru': "❌ Пожалуйста, введите корректный номер телефона:",
            'uz': "❌ Iltimos, to'g'ri telefon raqamini kiriting:"
        }
        await message.answer(error_messages.get(lang, error_messages['en']))
        return
    
    fullname = data.get('fullname')
    
    try:
        user = await User.create(
            id=message.from_user.id,
            fullname=fullname,
            phone_number=phone_number,
            username=message.from_user.username,
            language=lang,
            is_premium=False,
            total_spent=0,
            is_banned=False
        )
        
        success_messages = {
            'en': f"🎉 Registration complete!\n\nWelcome, {fullname}!\n\nYou can now browse our Premium packages:",
            'ru': f"🎉 Регистрация завершена!\n\nДобро пожаловать, {fullname}!\n\nТеперь вы можете просматривать наши Premium пакеты:",
            'uz': f"🎉 Ro'yxatdan o'tish yakunlandi!\n\nXush kelibsiz, {fullname}!\n\nEndi Premium paketlarni ko'rishingiz mumkin:"
        }
        
        await message.answer(
            success_messages.get(lang, success_messages['en']),
            reply_markup=main_menu(lang)
        )
        
        await state.clear()
        
    except Exception as e:
        error_messages = {
            'en': "❌ An error occurred during registration. Please try /start again.",
            'ru': "❌ Произошла ошибка при регистрации. Попробуйте /start снова.",
            'uz': "❌ Ro'yxatdan o'tishda xatolik yuz berdi. /start qayta yozing."
        }
        await message.answer(error_messages.get(lang, error_messages['en']))
        await state.clear()
        print(f"Registration error: {e}")


def get_phone_keyboard(lang='en'):
    """Keyboard with phone share button"""
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    
    button_texts = {
        'en': '📱 Share Phone Number',
        'ru': '📱 Отправить номер',
        'uz': '📱 Raqamni yuborish'
    }
    
    back_texts = {
        'en': '⬅️ Back',
        'ru': '⬅️ Назад',
        'uz': '⬅️ Orqaga'
    }
    
    buttons = [
        [KeyboardButton(text=button_texts.get(lang, button_texts['en']), request_contact=True)],
        [KeyboardButton(text=back_texts.get(lang, back_texts['en']))]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )