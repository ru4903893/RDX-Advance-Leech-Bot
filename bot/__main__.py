import asyncio
from pyrogram import Client
from bot.config import Config
from bot.database.mongodb import init_db
from bot.helpers.utils import load_modules

app = Client(
    "rdx-clone",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.TELEGRAM_API,
    api_hash=Config.TELEGRAM_HASH,
    workers=50,
    in_memory=True
)

async def main():
    await init_db()
    await load_modules(app)
    await app.start()
    print("🚀 Bot Started Successfully")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
