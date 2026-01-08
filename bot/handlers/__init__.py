from bot.dispacher import dp
from bot.handlers.main_handler import main_router
from bot.handlers.catalog_handler import catalog_router
from bot.handlers.payment_handler import payment_router
from bot.handlers.admin_handler import admin_router
from bot.handlers.profile_handler import profile_router
from bot.handlers.help_handler import help_router
from bot.handlers.language_handler import language_router

dp.include_routers(*[
    main_router,
    catalog_router,
    payment_router,
    admin_router,
    profile_router,
    help_router,
    language_router,
])