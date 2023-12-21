
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime

logging.basicConfig(level=logging.INFO)
router = Router()
async def print_msg(text, chat_id, bot: Bot):
    await bot.send_message(chat_id, text)

async def ping(text, chat_id, todo_id, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Сделано",
        callback_data="done" + (str)(todo_id))
    )
    builder.add(types.InlineKeyboardButton(
        text="Отложить",
        callback_data="defer"+ (str)(todo_id))
    )
    await bot.send_message(chat_id, text, reply_markup=builder.as_markup())


@router.callback_query(F.data[:4] == "done")
async def button_mark_as_done(callback: types.CallbackQuery):
    todo_id = int(callback.data[4:])
    # await mark_as_done(todo_id)
    await callback.message.answer("Отличная работа, задача выполнена")
    await callback.answer()

@router.callback_query(F.data[:5] == "defer")
async def button_defer(callback: types.CallbackQuery):
    todo_id = int(callback.data[5:])
    # await defer()
    await callback.message.answer("Отложено")
    await callback.answer()

async def print_todo_of_list(text, chat_id, todo_id, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Сделано",
        callback_data="done" + (str)(todo_id))
    )
    builder.add(types.InlineKeyboardButton(
        text="Удалить",
        callback_data="delete"+ (str)(todo_id))
    )
    await bot.send_message(chat_id, text, reply_markup=builder.as_markup())

@router.callback_query(F.data[:4] == "done")
async def button_mark_as_done(callback: types.CallbackQuery):
    todo_id = int(callback.data[4:])
    # await mark_as_done(todo_id)
    await callback.message.answer("Отличная работа, задача выполнена")
    await callback.answer()

@router.callback_query(F.data[:6] == "delete")
async def button_defer(callback: types.CallbackQuery):
    todo_id = int(callback.data[6:])
    # await defer(todo_id)
    await callback.message.answer("Удалено")
    await callback.answer()