import time

async def progress(current, total, message, start):
    now = time.time()
    diff = now - start
    if diff % 5 == 0:
        percent = current * 100 / total
        await message.edit(
            f"📊 Progress: {percent:.2f}%\n"
            f"{current // (1024*1024)}MB / {total // (1024*1024)}MB"
        )
