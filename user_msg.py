
import asyncio
import logging
from aiogram import  Router, types, F, Bot
from aiogram.filters.command import Command, CommandObject
from aiogram.types import Message
from aiogram.filters import Command
from datetime import datetime
from utilits import  create_new_job
from token_reading import bot

router = Router()

@router.message(Command("start"))

async def cmd_start(message: types.Message):
    await message.answer("Просто напишите задачу,\n /set_stat_freq число дней - изменить период подведения итогов\n /get_list список дел\n/get_report отчёт")

@router.message(Command("set_stat_freq"))

async def read_stat_freq(message: types.Message, command: CommandObject):
    new_freq = (str)(command.args)
    chat_id = message.from_user.id
    if (new_freq.isnumeric() and new_freq != ""):
        # await set_stat_freq(chat_id, new_freq)
        await bot.send_message(chat_id, "Период подведения итогов изменён")

    else:
        await bot.send_message(chat_id, "Введите необходимый период просто как число, например:\n/set_stat_freq 7")

@router.message(Command("get_list"))
async def cmd_get_list(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, "Ваш список дел:")
    # await get_list(chat_id)

@router.message(Command("get_report"))
async def cmd_get_report(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, "Ваш отчёт:")
    # await get_report(chat_id)

@router.message(F.text)

async def read_to_do(message: Message, bot: Bot, database):
    chat_id = message.from_user.id
    create_time = datetime.now()
    #await create_to_do(message.text, chat_id, create_time)
    await create_new_job(message.text, chat_id, database)
    await message.answer("Todo создана")

