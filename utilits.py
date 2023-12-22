from datetime import datetime
import asyncio
from sheduling import sched
from bot_msg import print_msg, ping
from database import *
from random import randint

#async def create_message(text,time_month,time_day,time_hour):

async def com_tobot1(text,chat_id, todo_id):#сообщение без дедлайна

    await ping("Это интервальная отправка сообщений"+" "+text,chat_id, todo_id)
#async def com_tobot2(text,time_month,time_day,time_hour):  # сообщение с дедлайном




#async def create_new_job_dl (text,time_month,time_day,time_hour):
    #sched.add_job(com_tobot2(text,time_month,time_day,time_hour),"cron",month=time_month,day=time_day,hour=time_hour  )


async def create_new_job(text,chat_id, db):
    # получение из бд todoid
    # todo_id = create(db, chat_id, text, datetime.now() + (datetime(2022, 4, 30, 12, 0, 4)- datetime(2022, 4, 30, 12, 0, 0)))
    todo_id = str(randint(1, 1000000))
    sched.add_job(com_tobot1, 'interval', args=[text,chat_id, todo_id], seconds = 2, id = todo_id)






