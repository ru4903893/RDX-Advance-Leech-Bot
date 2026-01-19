from pyrogram import filters
from bot import app
from bot.services.ytdlp import ytdlp_download
from bot.helpers.uploader import upload_file
import os

@app.on_message(filters.command("ytdlleech"))
async def ytdlleech(_, message):
    if len(message.command) == 1:
        return await message.reply("❌ Send a link")

    url = message.command[1]
    out = "downloads/ytdlp"

    ytdlp_download(url, out)

    for file in os.listdir(out):
        await upload_file(
            app,
            message.chat.id,
            f"{out}/{file}",
            "📤 yt-dlp Leech"
        )

    await message.reply("✅ yt-dlp Leech Completed")
