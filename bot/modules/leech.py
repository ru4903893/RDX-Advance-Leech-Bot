from pyrogram import filters
from bot import app

@app.on_message(filters.command("leech"))
async def leech(_, message):
    if len(message.command) == 1:
        return await message.reply("❌ Send a link to leech")

    link = message.text.split(maxsplit=1)[1]
    await message.reply(f"📤 Leech started:\n{link}")
