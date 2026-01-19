from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import app
from bot.config import Config

@app.on_message(filters.command("start"))
async def start(_, message):
    buttons = [
        [InlineKeyboardButton("📢 Channel", url="https://t.me/your_channel")],
        [InlineKeyboardButton("👤 Owner", url="https://t.me/your_username")],
        [InlineKeyboardButton("⚙ Settings", callback_data="usetting")]
    ]

    await message.reply_text(
        "👋 **Welcome to Advanced Leech & Mirror Bot**\n\n"
        "• Mirror to Google Drive\n"
        "• Leech to Telegram\n"
        "• Torrent / Direct / YTDLP\n\n"
        "**Use /help to see commands**",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
