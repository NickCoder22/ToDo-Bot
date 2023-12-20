import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from datetime import datetime

logging.basicConfig(level=logging.INFO)
bot = Bot(token="")

dp = Dispatcher()

async def print_msg(text, chat_id):
    await bot.send_message(chat_id, text)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Просто напишите задачу,\n /set_stat_freq число дней - изменить период подведения итогов")

@dp.message(Command("set_stat_freq"))

async def read_stat_freq(message: types.Message, command: CommandObject):
    new_freq = command.args
    chat_id = message.from_user.id
    #set_stat_freq(new_freq, chat_id)
    await message.answer("Период подведения итогов изменён")

@dp.message(F.text)

async def read_to_do(message: Message):
    chat_id = message.from_user.id
    create_time = datetime.now()
    #create_to_do(message.text, chat_id, create_time)
    await message.answer("Todo создана")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
