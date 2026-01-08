from aiogram.utils.i18n import FSMI18nMiddleware


async def all_middleware(dp):
    dp.update.middleware()
