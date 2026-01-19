from pyrogram import filters
from bot import app

HELP_TEXT = """
🚀 **Available Commands**

/mirror - Mirror to Google Drive
/leech - Leech to Telegram
/qbleech - Torrent leech (VPS)
/status - Show tasks
/cancel - Cancel task
/usetting - User settings
/bsetting - Bot settings
"""

@app.on_message(filters.command("help"))
async def help(_, message):
    await message.reply(HELP_TEXT)
