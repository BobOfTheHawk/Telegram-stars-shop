from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from utils.config import CF as conf

TOKEN = conf.bot.TOKEN
# Using docker
# redis_ = Redis(host='redis', port=6379)

# Without using docker
# redis = Redis()
#
#
# redis_storage = RedisStorage(redis)
# dp = Dispatcher(storage=redis_storage)
dp = Dispatcher()
