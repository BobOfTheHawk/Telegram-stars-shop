"""
Custom filters for bot handlers
"""
from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery
from utils.admin import is_admin


class IsAdmin(Filter):
    """Filter to check if user is admin"""
    
    async def __call__(self, message: Message) -> bool:
        return await is_admin(message.from_user.id)


class IsAdminCallback(Filter):
    """Filter for callback queries from admins"""
    
    async def __call__(self, callback: CallbackQuery) -> bool:
        return await is_admin(callback.from_user.id)