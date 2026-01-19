import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    OWNER_ID = int(os.getenv("OWNER_ID", 0))

    TELEGRAM_API = int(os.getenv("TELEGRAM_API"))
    TELEGRAM_HASH = os.getenv("TELEGRAM_HASH")

    DATABASE_URL = os.getenv("DATABASE_URL")

    DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "downloads")
    DEFAULT_UPLOAD = os.getenv("DEFAULT_UPLOAD", "gd")

    BOT_PM = os.getenv("BOT_PM", "True") == "True"
    SET_COMMANDS = os.getenv("SET_COMMANDS", "True") == "True"

    STATUS_UPDATE_INTERVAL = int(os.getenv("STATUS_UPDATE_INTERVAL", 2))
    STATUS_LIMIT = int(os.getenv("STATUS_LIMIT", 4))

    SUDO_USERS = set(map(int, os.getenv("SUDO_USERS", "").split())) if os.getenv("SUDO_USERS") else set()

    IS_HEROKU = bool(os.getenv("DYNO"))
