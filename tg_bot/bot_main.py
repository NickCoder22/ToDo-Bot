#новая ветка
import asyncio
import logging
from aiogram import Bot, Dispatcher
import user_msg
import bot_msg
#from user_msg import cmd_start, read_stat_freq, cmd_get_list, cmd_get_report, read_to_do
#from bot_msg import print_msg, ping, button_mark_as_done, button_defer, print_todo_of_list, button_mark_as_done, button_defer
from datetime import datetime

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token="")
    dp = Dispatcher()
    dp.include_routers(user_msg.router, bot_msg.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
