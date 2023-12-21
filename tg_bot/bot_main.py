import asyncio
import logging
from aiogram import Bot, Dispatcher
import user_msg
import bot_msg
from datetime import datetime
from token_reading import bot
logging.basicConfig(level=logging.INFO)

async def start_tg():
    dp = Dispatcher()
    dp.include_routers(user_msg.router, bot_msg.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
