from pyrogram import filters
from bot import app
from bot.database.tasks_db import update_task

@app.on_message(filters.command("cancel"))
async def cancel(_, message):
    if len(message.command) == 1:
        return await message.reply("❌ Send GID")

    gid = message.command[1]
    await update_task(gid, "Cancelled")
    await message.reply(f"❌ Task `{gid}` cancelled")

@app.on_message(filters.command("cancelall"))
async def cancelall(_, message):
    await message.reply("❌ All running tasks cancelled")
