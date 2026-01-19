import os
import time
from pyrogram.errors import FloodWait
import asyncio

async def upload_file(app, chat_id, file_path, caption):
    try:
        await app.send_document(
            chat_id=chat_id,
            document=file_path,
            caption=caption
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await upload_file(app, chat_id, file_path, caption)
