from datetime import datetime
from bot.config import Config

# Theme constants
LIGHT_THEME = "light"
DARK_THEME = "dark"

def get_current_theme():
    """
    Auto detect theme based on local time
    Day   → Light theme
    Night → Dark theme
    """
    try:
        hour = datetime.now().hour
        if hour >= 18 or hour < 6:
            return DARK_THEME
        return LIGHT_THEME
    except Exception:
        return LIGHT_THEME


def get_theme_name():
    """
    Returns custom bot theme name
    """
    return getattr(Config, "BOT_THEME", "CANDYCLOUD")


def get_emoji_style():
    """
    Emoji style based on theme
    """
    theme = get_current_theme()
    if theme == DARK_THEME:
        return {
            "ok": "🌙",
            "loading": "✨",
            "error": "❌",
            "file": "📁",
            "speed": "⚡",
            "progress": "📦",
            "time": "⏳"
        }
    else:
        return {
            "ok": "☀️",
            "loading": "🍭",
            "error": "❌",
            "file": "📁",
            "speed": "⚡",
            "progress": "📦",
            "time": "⏳"
        }
