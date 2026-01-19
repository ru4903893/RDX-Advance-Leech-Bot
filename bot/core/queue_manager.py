import asyncio

QUEUE = []
MAX_QUEUE = 3

async def add_queue(task):
    QUEUE.append(task)

async def process_queue():
    while True:
        if QUEUE:
            task = QUEUE.pop(0)
            await task()
        await asyncio.sleep(1)
