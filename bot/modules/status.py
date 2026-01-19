from pyrogram import filters
from bot import app
from bot.database.tasks_db import get_tasks

@app.on_message(filters.command("status"))
async def status(_, message):
    tasks = get_tasks()

    if not tasks:
        return await message.reply("🍭 No active tasks right now!")

    for task in tasks:
        text = (
            "📊 **CandyCloud Status** ☁️\n\n"
            f"📁 File: `{task.get('name', 'Unknown')}`\n"
            f"⚡ Speed: `{task.get('speed', 'N/A')}`\n"
            f"📦 Progress: `{task.get('progress', '0%')}`\n"
            f"⏳ ETA: `{task.get('eta', '∞')}`\n\n"
            "💖 Please wait, magic is happening…"
        )

        await message.reply_text(text)
