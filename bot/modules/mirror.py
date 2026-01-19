from pyrogram import filters
from bot import app
from bot.database.tasks_db import add_task
import uuid

@app.on_message(filters.command("mirror"))
async def mirror(_, message):
    if len(message.command) == 1:
        return await message.reply("❌ Send a direct link")

    link = message.text.split(maxsplit=1)[1]
    gid = str(uuid.uuid4())[:8]

    await add_task(gid, message.from_user.id, "Mirror Task", "Downloading")

    await message.reply(
        f"📥 **Mirror Started**\n"
        f"🆔 `{gid}`\n"
        f"🔗 {link}"
    )
