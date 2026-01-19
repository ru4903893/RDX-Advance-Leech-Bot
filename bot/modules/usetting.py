from pyrogram import filters
from bot import app
from bot.database.users_db import get_user, set_user

@app.on_message(filters.command("usetting"))
async def usetting(_, message):
    user_id = message.from_user.id
    user = await get_user(user_id) or {}

    text = (
        "⚙ **User Settings**\n\n"
        f"Upload Mode: `{user.get('upload', 'gd')}`\n\n"
        "Use:\n"
        "`/usetting upload gd`\n"
        "`/usetting upload tg`"
    )

    await message.reply(text)

@app.on_message(filters.command("usetting") & filters.regex("upload"))
async def set_upload(_, message):
    user_id = message.from_user.id
    mode = message.text.split()[-1]

    if mode not in ["gd", "tg"]:
        return await message.reply("❌ Invalid mode")

    await set_user(user_id, {"upload": mode})
    await message.reply(f"✅ Upload mode set to `{mode}`")

