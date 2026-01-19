from pyrogram import filters
from bot import app
from bot.services.qbittorrent import is_available
from bot.database.tasks_db import add_task

@app.on_message(filters.command("qbleech"))
async def qbleech(_, message):
    if not is_available():
        return await message.reply(
            "❌ qBittorrent is disabled on Heroku\n"
            "✅ Use VPS for this feature"
        )

    if len(message.command) == 1:
        return await message.reply("Send magnet or torrent link")

    link = message.text.split(maxsplit=1)[1]
    gid = f"qb-{message.id}"

    await add_task(
        gid=gid,
        user_id=message.from_user.id,
        name="Torrent Task",
        status="Downloading"
    )

    await message.reply(
        f"📥 **qBittorrent Leech Started**\n\n"
        f"🆔 `{gid}`\n"
        f"🔗 {link}"
    )
