from database import *
import asyncio
import datetime
import user_msg
import bot_msg
import logging
from aiogram import Bot, Dispatcher
from token_reading import bot
from sheduling import sched
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
logging.basicConfig(level=logging.INFO)

class Middleware(BaseMiddleware):
    def __init__(self, database):
        self._database = database

    async def __call__(self,handler,event,data):
        data["database"] = self._database
        return await handler(event, data)

async def main():
    # dbcfg = open("db.cfg")
    # address, user, passwd, ns, db = dbcfg.readline().split()
    sched.start()
    # db = await connect(user, passwd, ns, db)
    db = "db"
    dp = Dispatcher()
    dp.include_routers(user_msg.router, bot_msg.router)
    user_msg.router.message.middleware(Middleware(database=db))
    bot_msg.router.message.middleware(Middleware(database=db))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
