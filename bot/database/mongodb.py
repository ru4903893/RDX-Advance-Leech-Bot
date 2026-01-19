from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config

db = None

async def init_db():
    global db
    client = AsyncIOMotorClient(Config.DATABASE_URL)
    db = client["RDX"]
    print("✅ MongoDB Connected")
