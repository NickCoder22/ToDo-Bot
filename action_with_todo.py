import asyncio
from sheduling import sched

async def mark_as_done(todo_id):
    # нужно отметить в бд
    sched.remove_job(todo_id)


async def defer(todo_id):
    # нужно отметить в бд
    sched.reschedule_job(job_id=todo_id, trigger='interval', seconds = 10)