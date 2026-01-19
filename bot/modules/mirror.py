from pyrogram import filters
from bot import app

@app.on_message(filters.command("mirror"))
async def mirror(_, message):
    if len(message.command) == 1:
        return await message.reply("❌ Send a link to mirror")

    link = message.text.split(maxsplit=1)[1]
    await message.reply(f"📥 Mirroring started:\n{link}")
