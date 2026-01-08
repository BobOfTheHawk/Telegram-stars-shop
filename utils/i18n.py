"""
Internationalization (i18n) utilities
"""
from typing import Dict, Any

# Translation dictionaries
TRANSLATIONS = {
    'en': {
        # Main Menu
        'welcome_back': '👋 Welcome back, {name}!',
        'welcome_new': '👋 Welcome to Premium Telegram Bot!',
        'status': 'Status: {status}',
        'choose_option': 'Choose an option from the menu below:',
        'enter_fullname': 'Please enter your full name to get started:',
        'status_premium': '💎 Premium',
        'status_free': 'Free',
        
        # Buttons
        'btn_buy_premium': '🛒 Buy Premium',
        'btn_my_profile': '👤 My Profile',
        'btn_help': '❓ Help',
        'btn_back': '⬅️ Back',
        'btn_buy_now': '💳 Buy Now',
        'btn_confirm': '✅ Confirm Purchase',
        'btn_cancel': '❌ Cancel',
        
        # Store
        'store_welcome': '💎 <b>Welcome to Our Store!</b>',
        'store_subtitle': 'What would you like to purchase?',
        'category_premium_title': '🎁 <b>Telegram Premium</b>',
        'category_premium_desc': 'Unlock exclusive features and faster downloads',
        'category_stars_title': '⭐ <b>Telegram Stars</b>',
        'category_stars_desc': 'Buy digital goods and support creators',
        'choose_category': '👇 Choose a category below:',
        
        # Premium
        'premium_title': '💎 <b>Telegram Premium Packages</b>',
        'premium_features': 'Get exclusive features:',
        'feature_downloads': '• ⚡ Faster downloads',
        'feature_stickers': '• 🎨 Exclusive stickers & reactions',
        'feature_voice': '• 🎙️ Voice-to-text conversion',
        'feature_no_ads': '• 🚫 No ads',
        'feature_icon': '• 📱 Premium app icon',
        'feature_channels': '• 📢 Unlimited channels',
        'select_package': '👇 Select a package:',
        'save_percent': '🔥 Save {percent}%!',
        'per_month': '{price} UZS/month',
        
        # Stars
        'stars_title': '⭐ <b>Telegram Stars</b>',
        'stars_features': 'Use Stars to:',
        'stars_feature_gifts': '• 🎁 Send gifts to others',
        'stars_feature_creators': '• 💬 Support content creators',
        'stars_feature_stickers': '• 🎨 Buy premium stickers',
        'stars_feature_items': '• 🎮 Purchase in-app items',
        'per_star': '~{price} UZS per star',
        
        # Product Details
        'duration': '📅 <b>Duration:</b> {months} month(s)',
        'price': '💰 <b>Price:</b> {price} UZS',
        'amount': '⭐ <b>Amount:</b> {amount} Stars',
        'you_save': '🎉 <b>You save:</b> {amount} UZS ({percent}% off!)',
        'premium_features_title': '✨ <b>Premium Features:</b>',
        'ready_to_purchase': '👇 Ready to purchase?',
        'delivered_fast': '⚡ Delivered within 1-2 minutes!',
        
        # Payment
        'purchase_confirmation': '💳 <b>Purchase Confirmation</b>',
        'product': '📦 Product: {product}',
        'confirm_purchase': '✅ Click \'Confirm Purchase\' to proceed with payment.',
        'invoice_sent': '💳 <b>Invoice sent!</b>',
        'click_pay': 'Click the \'Pay\' button to complete your purchase.',
        
        # Success
        'payment_success': '🎉 <b>Payment Successful!</b>',
        'premium_code': '✅ Your Premium Gift Code:',
        'how_to_redeem': '📱 <b>How to redeem:</b>',
        'redeem_step1': '1. Tap on the code to copy it',
        'redeem_step2': '2. Open Telegram Settings',
        'redeem_step3': '3. Tap \'Telegram Premium\'',
        'redeem_step4': '4. Tap \'Have a gift code?\'',
        'redeem_step5': '5. Paste and activate',
        'enjoy_premium': '💎 Enjoy your {months} month(s) of Premium!',
        'payment_confirmed': '✅ Payment confirmed: {amount} UZS',
        'processing': '⏳ Processing... You\'ll receive your Stars within 1-2 minutes!',
        'order_id': 'Order ID: #{id}',
        
        # Profile
        'your_profile': '👤 <b>Your Profile</b>',
        'name': '📛 Name: {name}',
        'user_id': '🆔 User ID: {id}',
        'username': '📱 Username: @{username}',
        'member_since': '📅 Member since: {date}',
        'premium_active': '💎 <b>Status: Premium Active</b>',
        'expires': '⏰ Expires: {date}',
        'days_remaining': '📆 Days remaining: {days} days',
        'status_free_title': '🆓 <b>Status: Free</b>',
        'upgrade_prompt': '💡 Upgrade to Premium to unlock exclusive features!',
        'your_stats': '💰 <b>Your Statistics:</b>',
        'total_spent': 'Total spent: {amount} UZS',
        'total_orders': 'Total orders: {count}',
        'ready_upgrade': '🛒 Ready to upgrade? Tap \'Buy Premium\' below!',
        
        # Help
        'help_title': '❓ <b>Help & FAQ</b>',
        'help_how_to_buy': '<b>📱 How to Buy:</b>',
        'help_about_premium': '<b>💎 About Premium:</b>',
        'help_about_stars': '<b>⭐ About Stars:</b>',
        'help_payment': '<b>💳 Payment:</b>',
        'help_delivery': '<b>📦 Delivery:</b>',
        'help_support': '<b>👨‍💻 Support:</b>',
        
        # Errors
        'error_not_available': '❌ This product is no longer available',
        'error_user_not_found': '❌ User not found. Please use /start to register.',
        'no_orders': '📭 No orders yet.',
        'start_shopping': 'Start shopping by tapping \'Buy Premium\' below!',
    },
    
    'ru': {
        # Main Menu
        'welcome_back': '👋 С возвращением, {name}!',
        'welcome_new': '👋 Добро пожаловать в Premium Telegram Bot!',
        'status': 'Статус: {status}',
        'choose_option': 'Выберите опцию из меню ниже:',
        'enter_fullname': 'Пожалуйста, введите ваше полное имя:',
        'status_premium': '💎 Премиум',
        'status_free': 'Бесплатно',
        
        # Buttons
        'btn_buy_premium': '🛒 Купить Премиум',
        'btn_my_profile': '👤 Мой Профиль',
        'btn_help': '❓ Помощь',
        'btn_back': '⬅️ Назад',
        'btn_buy_now': '💳 Купить',
        'btn_confirm': '✅ Подтвердить',
        'btn_cancel': '❌ Отмена',
        
        # Store
        'store_welcome': '💎 <b>Добро пожаловать в наш магазин!</b>',
        'store_subtitle': 'Что вы хотите приобрести?',
        'category_premium_title': '🎁 <b>Telegram Premium</b>',
        'category_premium_desc': 'Разблокируйте эксклюзивные функции',
        'category_stars_title': '⭐ <b>Telegram Stars</b>',
        'category_stars_desc': 'Покупайте цифровые товары',
        'choose_category': '👇 Выберите категорию:',
        
        # Premium
        'premium_title': '💎 <b>Пакеты Telegram Premium</b>',
        'premium_features': 'Получите эксклюзивные функции:',
        'feature_downloads': '• ⚡ Быстрая загрузка',
        'feature_stickers': '• 🎨 Эксклюзивные стикеры',
        'feature_voice': '• 🎙️ Голос в текст',
        'feature_no_ads': '• 🚫 Без рекламы',
        'feature_icon': '• 📱 Премиум иконка',
        'feature_channels': '• 📢 Без лимита каналов',
        'select_package': '👇 Выберите пакет:',
        'save_percent': '🔥 Скидка {percent}%!',
        'per_month': '{price} UZS/месяц',
        
        # Stars
        'stars_title': '⭐ <b>Telegram Stars</b>',
        'stars_features': 'Используйте Stars для:',
        'stars_feature_gifts': '• 🎁 Отправки подарков',
        'stars_feature_creators': '• 💬 Поддержки авторов',
        'stars_feature_stickers': '• 🎨 Покупки стикеров',
        'stars_feature_items': '• 🎮 Покупки в приложении',
        'per_star': '~{price} UZS за звезду',
        
        # Product Details
        'duration': '📅 <b>Длительность:</b> {months} мес.',
        'price': '💰 <b>Цена:</b> {price} UZS',
        'amount': '⭐ <b>Количество:</b> {amount} Stars',
        'you_save': '🎉 <b>Экономия:</b> {amount} UZS ({percent}%!)',
        'premium_features_title': '✨ <b>Премиум функции:</b>',
        'ready_to_purchase': '👇 Готовы купить?',
        'delivered_fast': '⚡ Доставка за 1-2 минуты!',
        
        # Payment
        'purchase_confirmation': '💳 <b>Подтверждение покупки</b>',
        'product': '📦 Товар: {product}',
        'confirm_purchase': '✅ Нажмите \'Подтвердить\' для оплаты.',
        'invoice_sent': '💳 <b>Счет отправлен!</b>',
        'click_pay': 'Нажмите кнопку \'Оплатить\'.',
        
        # Success
        'payment_success': '🎉 <b>Оплата успешна!</b>',
        'premium_code': '✅ Ваш код Premium:',
        'how_to_redeem': '📱 <b>Как активировать:</b>',
        'redeem_step1': '1. Скопируйте код',
        'redeem_step2': '2. Откройте настройки Telegram',
        'redeem_step3': '3. Нажмите \'Telegram Premium\'',
        'redeem_step4': '4. Нажмите \'Есть код?\'',
        'redeem_step5': '5. Вставьте и активируйте',
        'enjoy_premium': '💎 Наслаждайтесь {months} мес. Premium!',
        'payment_confirmed': '✅ Оплата подтверждена: {amount} UZS',
        'processing': '⏳ Обработка... Получите Stars за 1-2 минуты!',
        'order_id': 'Заказ №{id}',
        
        # Profile
        'your_profile': '👤 <b>Ваш профиль</b>',
        'name': '📛 Имя: {name}',
        'user_id': '🆔 ID: {id}',
        'username': '📱 Username: @{username}',
        'member_since': '📅 С нами с: {date}',
        'premium_active': '💎 <b>Статус: Premium активен</b>',
        'expires': '⏰ Истекает: {date}',
        'days_remaining': '📆 Осталось дней: {days}',
        'status_free_title': '🆓 <b>Статус: Бесплатно</b>',
        'upgrade_prompt': '💡 Обновитесь до Premium!',
        'your_stats': '💰 <b>Статистика:</b>',
        'total_spent': 'Потрачено: {amount} UZS',
        'total_orders': 'Заказов: {count}',
        'ready_upgrade': '🛒 Готовы? Нажмите \'Купить Premium\'!',
        
        # Help
        'help_title': '❓ <b>Помощь</b>',
        'help_how_to_buy': '<b>📱 Как купить:</b>',
        'help_about_premium': '<b>💎 О Premium:</b>',
        'help_about_stars': '<b>⭐ О Stars:</b>',
        'help_payment': '<b>💳 Оплата:</b>',
        'help_delivery': '<b>📦 Доставка:</b>',
        'help_support': '<b>👨‍💻 Поддержка:</b>',
        
        # Errors
        'error_not_available': '❌ Товар недоступен',
        'error_user_not_found': '❌ Пользователь не найден. Используйте /start.',
        'no_orders': '📭 Нет заказов.',
        'start_shopping': 'Начните с кнопки \'Купить Premium\'!',
    },
    
    'uz': {
        # Main Menu
        'welcome_back': '👋 Xush kelibsiz, {name}!',
        'welcome_new': '👋 Premium Telegram Botga xush kelibsiz!',
        'status': 'Status: {status}',
        'choose_option': 'Quyidagi menyudan tanlang:',
        'enter_fullname': 'Iltimos, to\'liq ismingizni kiriting:',
        'status_premium': '💎 Premium',
        'status_free': 'Bepul',
        
        # Buttons
        'btn_buy_premium': '🛒 Premium Sotib Olish',
        'btn_my_profile': '👤 Mening Profilim',
        'btn_help': '❓ Yordam',
        'btn_back': '⬅️ Orqaga',
        'btn_buy_now': '💳 Sotib Olish',
        'btn_confirm': '✅ Tasdiqlash',
        'btn_cancel': '❌ Bekor qilish',
        
        # Store
        'store_welcome': '💎 <b>Do\'konimizga xush kelibsiz!</b>',
        'store_subtitle': 'Nima sotib olmoqchisiz?',
        'category_premium_title': '🎁 <b>Telegram Premium</b>',
        'category_premium_desc': 'Maxsus funksiyalardan foydalaning',
        'category_stars_title': '⭐ <b>Telegram Stars</b>',
        'category_stars_desc': 'Raqamli mahsulotlar sotib oling',
        'choose_category': '👇 Kategoriyani tanlang:',
        
        # Premium
        'premium_title': '💎 <b>Telegram Premium Paketlar</b>',
        'premium_features': 'Maxsus imkoniyatlar:',
        'feature_downloads': '• ⚡ Tez yuklab olish',
        'feature_stickers': '• 🎨 Maxsus stikerlar',
        'feature_voice': '• 🎙️ Ovozdan matnga',
        'feature_no_ads': '• 🚫 Reklamasiz',
        'feature_icon': '• 📱 Premium belgi',
        'feature_channels': '• 📢 Cheksiz kanallar',
        'select_package': '👇 Paketni tanlang:',
        'save_percent': '🔥 {percent}% tejang!',
        'per_month': '{price} UZS/oy',
        
        # Stars
        'stars_title': '⭐ <b>Telegram Stars</b>',
        'stars_features': 'Stars bilan:',
        'stars_feature_gifts': '• 🎁 Sovg\'a yuboring',
        'stars_feature_creators': '• 💬 Kontentchilarni qo\'llab-quvvatlang',
        'stars_feature_stickers': '• 🎨 Stikerlar sotib oling',
        'stars_feature_items': '• 🎮 Ilova ichida xarid',
        'per_star': '~{price} UZS har bir yulduz',
        
        # Product Details
        'duration': '📅 <b>Muddati:</b> {months} oy',
        'price': '💰 <b>Narxi:</b> {price} UZS',
        'amount': '⭐ <b>Miqdori:</b> {amount} Stars',
        'you_save': '🎉 <b>Tejaysiz:</b> {amount} UZS ({percent}%!)',
        'premium_features_title': '✨ <b>Premium imkoniyatlar:</b>',
        'ready_to_purchase': '👇 Sotib olasizmi?',
        'delivered_fast': '⚡ 1-2 daqiqada yetkazib beriladi!',
        
        # Payment
        'purchase_confirmation': '💳 <b>Xaridni tasdiqlash</b>',
        'product': '📦 Mahsulot: {product}',
        'confirm_purchase': '✅ To\'lovni davom ettirish uchun bosing.',
        'invoice_sent': '💳 <b>Hisob-faktura yuborildi!</b>',
        'click_pay': '\'To\'lash\' tugmasini bosing.',
        
        # Success
        'payment_success': '🎉 <b>To\'lov muvaffaqiyatli!</b>',
        'premium_code': '✅ Premium kodingiz:',
        'how_to_redeem': '📱 <b>Qanday faollashtirish:</b>',
        'redeem_step1': '1. Kodni nusxalang',
        'redeem_step2': '2. Telegram sozlamalarini oching',
        'redeem_step3': '3. \'Telegram Premium\' bosing',
        'redeem_step4': '4. \'Kod bormi?\' bosing',
        'redeem_step5': '5. Joylashtiring va faollashtiring',
        'enjoy_premium': '💎 {months} oy Premium\'dan bahramand bo\'ling!',
        'payment_confirmed': '✅ To\'lov tasdiqlandi: {amount} UZS',
        'processing': '⏳ Qayta ishlanmoqda... 1-2 daqiqada Stars olasiz!',
        'order_id': 'Buyurtma №{id}',
        
        # Profile
        'your_profile': '👤 <b>Sizning profilingiz</b>',
        'name': '📛 Ism: {name}',
        'user_id': '🆔 ID: {id}',
        'username': '📱 Username: @{username}',
        'member_since': '📅 A\'zo: {date}',
        'premium_active': '💎 <b>Status: Premium faol</b>',
        'expires': '⏰ Tugaydi: {date}',
        'days_remaining': '📆 Qolgan kunlar: {days}',
        'status_free_title': '🆓 <b>Status: Bepul</b>',
        'upgrade_prompt': '💡 Premium\'ga o\'ting!',
        'your_stats': '💰 <b>Statistika:</b>',
        'total_spent': 'Sarflangan: {amount} UZS',
        'total_orders': 'Buyurtmalar: {count}',
        'ready_upgrade': '🛒 Tayyormisiz? \'Premium Sotib Olish\' bosing!',
        
        # Help
        'help_title': '❓ <b>Yordam</b>',
        'help_how_to_buy': '<b>📱 Qanday sotib olish:</b>',
        'help_about_premium': '<b>💎 Premium haqida:</b>',
        'help_about_stars': '<b>⭐ Stars haqida:</b>',
        'help_payment': '<b>💳 To\'lov:</b>',
        'help_delivery': '<b>📦 Yetkazib berish:</b>',
        'help_support': '<b>👨‍💻 Qo\'llab-quvvatlash:</b>',
        
        # Errors
        'error_not_available': '❌ Mahsulot mavjud emas',
        'error_user_not_found': '❌ Foydalanuvchi topilmadi. /start yozing.',
        'no_orders': '📭 Buyurtmalar yo\'q.',
        'start_shopping': '\'Premium Sotib Olish\' bosing!',
    }
}


def get_text(lang: str, key: str, **kwargs) -> str:
    """
    Get translated text
    
    Args:
        lang: Language code ('en', 'ru', 'uz')
        key: Translation key
        **kwargs: Format parameters
    
    Returns:
        Translated and formatted text
    """
    # Default to English if language not found
    if lang not in TRANSLATIONS:
        lang = 'en'
    
    # Get translation
    text = TRANSLATIONS[lang].get(key, TRANSLATIONS['en'].get(key, key))
    
    # Format with parameters
    try:
        return text.format(**kwargs)
    except KeyError:
        return text