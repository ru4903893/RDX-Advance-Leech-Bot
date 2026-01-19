from pyrogram import filters
from bot import app
from bot.database.tasks_db import get_tasks

@app.on_message(filters.command("status"))
async def status(_, message):
    text = "📊 **Active Tasks**\n\n"
    async for task in get_tasks():
        text += f"• `{task['_id']}` | {task['name']} | **{task['status']}**\n"

    await message.reply(text if text.strip() else "❌ No active tasks")
