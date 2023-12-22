from database import *
import asyncio
import datetime
import user_msg
import bot_msg
import logging
from aiogram import Bot, Dispatcher
from token_reading import bot
from sheduling import sched
logging.basicConfig(level=logging.INFO)

async def main():
    dbcfg = open("db.cfg")
    address, user, passwd, ns, db = dbcfg.readline().split()
    sched.start()
    db = await connect(user, passwd, ns, db)
    dp = Dispatcher()
    dp.include_routers(user_msg.router, bot_msg.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
