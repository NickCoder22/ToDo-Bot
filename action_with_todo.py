import asyncio
from sheduling import sched

async def mark_as_done(todo_id):
    # нужно отметить в бд
    sched.remove_job(todo_id)