from datetime import datetime
import asyncio
from sheduling import sched
from bot_msg import print_msg

#async def create_message(text,time_month,time_day,time_hour):

async def com_tobot1(text,chat_id, bot):#сообщение без дедлайна

    await print_msg("Это интервальная отправка сообщений"+" "+text,chat_id, bot)
#async def com_tobot2(text,time_month,time_day,time_hour):  # сообщение с дедлайном




#async def create_new_job_dl (text,time_month,time_day,time_hour):
    #sched.add_job(com_tobot2(text,time_month,time_day,time_hour),"cron",month=time_month,day=time_day,hour=time_hour  )


async def create_new_job(text,chat_id, bot):
    sched.add_job(com_tobot1, 'interval', args=[text,chat_id, bot], seconds=1)






