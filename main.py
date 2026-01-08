import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from sqlalchemy.orm import sessionmaker
from utils.admin import initialize_admin
from utils.config import CF
import os
from bot.dispacher import TOKEN
from bot.handlers import dp
from bot.middilwares import all_middleware
from db import Config
from utils.config import WB

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Config.engine)


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{WB.BASE_WEBHOOK_URL}{WB.WEBHOOK_PATH}", secret_token=WB.WEBHOOK_SECRET)


async def main_webhook() -> web.Application:
    """Webhook mode - for production"""
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await all_middleware(dp)
    
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WB.WEBHOOK_SECRET,
    )
    webhook_requests_handler.register(app, path=WB.WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    dp.startup.register(on_startup)
    
    return app


async def main_polling(bot: Bot) -> None:
    """Polling mode - for local development"""
    await all_middleware(dp)
    await dp.start_polling(bot)


async def start_bot():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    initial_admin_id = int(os.getenv("INITIAL_ADMIN_ID", "6635413428"))
    await initialize_admin(initial_admin_id)
    
    # Check if we should use webhook or polling
    if WB.USE_WEBHOOK:
        # Webhook mode (production)
        app = await main_webhook()
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, WB.WEB_SERVER_HOST, WB.WEB_SERVER_PORT)
        await site.start()
        print(f"Bot started with webhook at {WB.BASE_WEBHOOK_URL}{WB.WEBHOOK_PATH}")
        
        # Keep running forever
        try:
            await asyncio.Event().wait()
        except KeyboardInterrupt:
            print("\nShutting down webhook...")
            await runner.cleanup()
    else:
        # Polling mode (local development)
        print("Bot started in polling mode (local development)")
        await main_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("\nBot stopped gracefully")