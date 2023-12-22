import asyncio
import logging
from aiogram import Bot, Dispatcher
import user_msg
import bot_msg
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from sheduling import sched
from bot_main import start_tg
logging.basicConfig(level=logging.INFO)

async def main():
    sched.start()
    await start_tg()

    print('STARTED')


if __name__ == "__main__":
    asyncio.run(main())