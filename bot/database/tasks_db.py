from bot.database.mongodb import db

async def add_task(gid, user_id, name, status):
    await db.tasks.insert_one({
        "_id": gid,
        "user_id": user_id,
        "name": name,
        "status": status
    })

async def update_task(gid, status):
    await db.tasks.update_one(
        {"_id": gid},
        {"$set": {"status": status}}
    )

async def get_tasks():
    return db.tasks.find()
