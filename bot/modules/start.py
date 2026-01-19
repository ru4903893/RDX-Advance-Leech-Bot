from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import app

@app.on_message(filters.command("start"))
async def start(_, message):

    text = (
        "✨ **Welcome to CandyCloud Mirror Bot** ☁️🍭\n\n"
        "🚀 **What I Can Do For You:**\n"
        "• 📥 Mirror files to Google Drive\n"
        "• 📤 Leech files to Telegram\n"
        "• 🧲 Torrent / Magnet Support\n"
        "• 🎬 YouTube & yt-dl sites\n\n"
        "⚡ **Fast • Clean • Reliable**\n\n"
        "👇 Choose an option below"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📥 Mirror", callback_data="mirror"),
            InlineKeyboardButton("📤 Leech", callback_data="leech")
        ],
        [
            InlineKeyboardButton("⚙ User Settings", callback_data="usetting")
        ],
        [
            InlineKeyboardButton("📢 Channel", url="https://t.me/YOUR_CHANNEL"),
            InlineKeyboardButton("👤 Owner", url="https://t.me/YOUR_USERNAME")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)
