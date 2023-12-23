from datetime import datetime
import asyncio
from sheduling import sched
from bot_msg import *
from database import *
from random import randint

#async def create_message(text,time_month,time_day,time_hour):
async def datetime_after_seconds(delta_sec):
    return datetime.now() + (datetime(0, 0, 0, 0, 0, delta_sec)- datetime(0, 0, 0, 0, 0, 0))

async def com_tobot1(text,chat_id, todo_id, db):#сообщение без дедлайна

    await ping("Это интервальная отправка сообщений"+" "+text,chat_id, todo_id, db)
#async def com_tobot2(text,time_month,time_day,time_hour):  # сообщение с дедлайном




#async def create_new_job_dl (text,time_month,time_day,time_hour):
    #sched.add_job(com_tobot2(text,time_month,time_day,time_hour),"cron",month=time_month,day=time_day,hour=time_hour  )


async def create_new_job(text,chat_id, db):
    # получение из бд todoid
    # todo_id = create(db, chat_id, text, datetime.now() + (datetime(2022, 4, 30, 12, 0, x)- datetime(2022, 4, 30, 12, 0, 0)))
    freq = 3
    todo_id = simple_create_todo(chat_id, text, None, datetime_after_seconds(freq), freq)
    sched.add_job(com_tobot1, 'interval', args=[text,chat_id, todo_id, db], seconds = freq, id = todo_id)
    
async def get_list(chat_id, db):
    list_without_deadline = simple_get_report_without_deadline(chat_id)
    print(list_without_deadline)
    for todo_id in list_without_deadline:
        todo = simple_get_todo(todo_id)
        await print_todo_of_list(todo["problem"], chat_id, todo_id, db)
    






