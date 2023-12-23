import asyncio
from sheduling import sched
from database import *
from datetime import datetime
async def datetime_after_seconds(delta_sec):
    return datetime.now() + (datetime(0, 0, 0, 0, 0, delta_sec)- datetime(0, 0, 0, 0, 0, 0))

async def mark_as_done(todo_id, database):
    # нужно отметить в бд
    sched.remove_job(todo_id)


async def defer(todo_id, database):
    # нужно отметить в бд
    todo = simple_get_todo(todo_id)
    next_ping_delta = todo["next_ping_delta"] * 1.5
    simple_remove_todo(todo_id)
    simple_create_todo(todo["chat_id"], todo["problem"], todo["deadline"], datetime_after_seconds(next_ping_delta), next_ping_delta)
    sched.reschedule_job(job_id=todo_id, trigger='interval', seconds = next_ping_delta)
    
async def delete(todo_id, database):
    # нужно отметить в бд
    simple_remove_todo(todo_id)
    sched.remove_job(todo_id)