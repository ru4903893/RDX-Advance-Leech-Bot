from bot.database.mongodb import db

async def get_user(user_id):
    return await db.users.find_one({"_id": user_id})

async def set_user(user_id, data):
    await db.users.update_one(
        {"_id": user_id},
        {"$set": data},
        upsert=True
    )

