from pyrogram import filters
from bot import app
from bot.services.ytdlp import ytdlp_download
from bot.services.drive import upload_to_drive
import os

@app.on_message(filters.command("ytdlmirror"))
async def ytdlmirror(_, message):
    if len(message.command) == 1:
        return await message.reply("❌ Send a link")

    url = message.command[1]
    out = "downloads/ytdlp"

    ytdlp_download(url, out)
    upload_to_drive(out, "yt-dlp")

    await message.reply("✅ yt-dlp Mirror Completed")
