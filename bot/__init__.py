from pyrogram import Client
from bot.config import Config

app = Client(
    "adv-kpsml",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.TELEGRAM_API,
    api_hash=Config.TELEGRAM_HASH,
    workers=50,
    in_memory=True
)
