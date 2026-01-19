from pyrogram import filters
from bot import app
from bot.config import Config

@app.on_message(filters.command("bsetting"))
async def bsetting(_, message):
    if message.from_user.id != Config.OWNER_ID:
        return await message.reply("❌ Owner only")

    await message.reply(
        "🤖 **Bot Settings**\n\n"
        f"Heroku Mode: `{Config.IS_HEROKU}`\n"
        "qBittorrent: Auto Detect\n"
    )
