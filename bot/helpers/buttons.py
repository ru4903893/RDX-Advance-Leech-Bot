from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url="https://t.me/your_channel")],
        [InlineKeyboardButton("👤 Owner", url="https://t.me/your_username")],
        [InlineKeyboardButton("⚙ User Settings", callback_data="usetting")]
    ])
