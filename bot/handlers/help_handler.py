from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from db.models import User
from utils.i18n import get_text

help_router = Router()


@help_router.message(Command("help"))
@help_router.message(F.text.contains("Help"))
@help_router.message(F.text.contains("Помощь"))
@help_router.message(F.text.contains("Yordam"))
async def show_help(message: Message):
    """Show help and FAQ"""
    
    user = await User.get(message.from_user.id)
    lang = user.language if user else 'en'
    
    help_texts = {
        'en': (
            "❓ <b>Help & FAQ</b>\n\n"
            
            "<b>📱 How to Buy:</b>\n"
            "1. Click '🛒 Buy Premium' button\n"
            "2. Choose Premium or Stars\n"
            "3. Select a package\n"
            "4. Click 'Buy Now'\n"
            "5. Complete payment\n\n"
            
            "<b>💎 About Premium:</b>\n"
            "Telegram Premium gives you exclusive features like faster downloads, "
            "no ads, unlimited channels, and much more!\n\n"
            
            "<b>⭐ About Stars:</b>\n"
            "Telegram Stars are virtual currency used to buy digital goods, "
            "send gifts, and support content creators.\n\n"
            
            "<b>💳 Payment:</b>\n"
            "We accept payments in UZS via Telegram's secure payment system.\n\n"
            
            "<b>📦 Delivery:</b>\n"
            "• Premium: Instant (gift code)\n"
            "• Stars: 1-2 minutes\n\n"
            
            "<b>🔄 Refunds:</b>\n"
            "Contact our support team if you have any issues.\n\n"
            
            "<b>🌍 Language:</b>\n"
            "Change language: /language\n\n"
            
            "<b>📚 Commands:</b>\n"
            "/start - Main menu\n"
            "/catalog - Browse products\n"
            "/profile - View your profile\n"
            "/orders - Order history\n"
            "/language - Change language\n"
            "/help - Show this message\n\n"
            
            "💬 Have questions? Feel free to ask!"
        ),
        'ru': (
            "❓ <b>Помощь</b>\n\n"
            
            "<b>📱 Как купить:</b>\n"
            "1. Нажмите '🛒 Купить Премиум'\n"
            "2. Выберите Premium или Stars\n"
            "3. Выберите пакет\n"
            "4. Нажмите 'Купить'\n"
            "5. Завершите оплату\n\n"
            
            "<b>💎 О Premium:</b>\n"
            "Telegram Premium дает вам эксклюзивные функции: быстрая загрузка, "
            "без рекламы, без лимита каналов и многое другое!\n\n"
            
            "<b>⭐ О Stars:</b>\n"
            "Telegram Stars - виртуальная валюта для покупки цифровых товаров, "
            "отправки подарков и поддержки авторов.\n\n"
            
            "<b>💳 Оплата:</b>\n"
            "Принимаем платежи в UZS через безопасную систему Telegram.\n\n"
            
            "<b>📦 Доставка:</b>\n"
            "• Premium: Мгновенно (код подарка)\n"
            "• Stars: 1-2 минуты\n\n"
            
            "<b>🔄 Возврат:</b>\n"
            "Свяжитесь с поддержкой при возникновении проблем.\n\n"
            
            "<b>🌍 Язык:</b>\n"
            "Изменить язык: /language\n\n"
            
            "<b>📚 Команды:</b>\n"
            "/start - Главное меню\n"
            "/catalog - Каталог товаров\n"
            "/profile - Ваш профиль\n"
            "/orders - История заказов\n"
            "/language - Изменить язык\n"
            "/help - Эта справка\n\n"
            
            "💬 Есть вопросы? Спрашивайте!"
        ),
        'uz': (
            "❓ <b>Yordam</b>\n\n"
            
            "<b>📱 Qanday sotib olish:</b>\n"
            "1. '🛒 Premium Sotib Olish' bosing\n"
            "2. Premium yoki Stars tanlang\n"
            "3. Paketni tanlang\n"
            "4. 'Sotib Olish' bosing\n"
            "5. To'lovni bajaring\n\n"
            
            "<b>💎 Premium haqida:</b>\n"
            "Telegram Premium sizga maxsus imkoniyatlar beradi: tez yuklab olish, "
            "reklamasiz, cheksiz kanallar va ko'p boshqalar!\n\n"
            
            "<b>⭐ Stars haqida:</b>\n"
            "Telegram Stars - raqamli mahsulotlar sotib olish, "
            "sovg'alar yuborish va kontentchilarni qo'llab-quvvatlash uchun valyuta.\n\n"
            
            "<b>💳 To'lov:</b>\n"
            "Telegram'ning xavfsiz to'lov tizimi orqali UZS qabul qilamiz.\n\n"
            
            "<b>📦 Yetkazib berish:</b>\n"
            "• Premium: Bir zumda (sovg'a kodi)\n"
            "• Stars: 1-2 daqiqa\n\n"
            
            "<b>🔄 Qaytarish:</b>\n"
            "Muammolar bo'lsa qo'llab-quvvatlash bilan bog'laning.\n\n"
            
            "<b>🌍 Til:</b>\n"
            "Tilni o'zgartirish: /language\n\n"
            
            "<b>📚 Buyruqlar:</b>\n"
            "/start - Asosiy menyu\n"
            "/catalog - Mahsulotlar\n"
            "/profile - Sizning profilingiz\n"
            "/orders - Buyurtmalar tarixi\n"
            "/language - Tilni o'zgartirish\n"
            "/help - Bu yordam\n\n"
            
            "💬 Savollar bormi? So'rang!"
        )
    }
    
    await message.answer(help_texts.get(lang, help_texts['en']))