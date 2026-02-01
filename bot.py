# ================== CONFIG (EDIT THIS ONLY) ==================
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")          # Heroku Config Vars
TMDB_API_KEY = os.getenv("TMDB_API_KEY")    # Heroku Config Vars
APP_URL = os.getenv("APP_URL")              # e.g. https://your-app.herokuapp.com

NETWORK_TAG = "@rdxmovie_hd"

# ✅ All OMDB API Keys (hardcoded)
OMDB_KEYS = [
    "ec03f6bd",
    "78aba0e3",
    "984f89be",
    "ce245f40",
    "2e8c5c65",
    "2451f643",
    "79803fd4",
    "f31bb8de",
    "ae54521d"
]

# ================== DO NOT EDIT BELOW ==================
import requests
from itertools import cycle
from telegram.ext import Updater, CommandHandler

TMDB_IMG = "https://image.tmdb.org/t/p/original"
omdb_cycle = cycle(OMDB_KEYS)


def tmdb_search(title, year=None):
    params = {"api_key": TMDB_API_KEY, "query": title}
    if year:
        params["year"] = year
    r = requests.get("https://api.themoviedb.org/3/search/multi", params=params).json()
    return r.get("results", [None])[0]


def tmdb_details(media_type, tmdb_id):
    url = f"https://api.themoviedb.org/3/{media_type}/{tmdb_id}"
    return requests.get(url, params={"api_key": TMDB_API_KEY}).json()


def omdb_fetch(imdb_id):
    if not imdb_id:
        return {}
    for _ in range(len(OMDB_KEYS)):
        r = requests.get(
            "http://www.omdbapi.com/",
            params={"apikey": next(omdb_cycle), "i": imdb_id}
        ).json()
        if r.get("Response") == "True":
            return r
    return {}


def shorten(text, limit=160):
    if not text:
        return ""
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "..."


def hashtags(genres):
    return " ".join("#" + g["name"].replace(" ", "") for g in genres)


def format_caption(tmdb, omdb):
    title = tmdb.get("title") or tmdb.get("name") or "N/A"
    released = tmdb.get("release_date") or tmdb.get("first_air_date") or "N/A"
    imdb = omdb.get("imdbRating", "N/A")

    rt = "00%"
    for r in omdb.get("Ratings", []):
        if "Rotten" in r.get("Source", ""):
            rt = r.get("Value")

    summary = shorten(tmdb.get("tagline") or tmdb.get("overview") or omdb.get("Plot"))
    synopsis = shorten(tmdb.get("overview") or omdb.get("Plot"), 260)

    return (
        f"*{title}* : {summary}\n\n"
        "*⟣────────────────────⟢*\n"
        "*‣ Audio ⌯[Hindi ]\n"
        f"‣ Rating ⌯ {imdb} IMDB | {rt} RT\n"
        "‣ Quality ⌯ 480p | 720p | 1080p\n"
        f"‣ Released On ⌯ {released}\n"
        f"‣ Genres ⌯* {hashtags(tmdb.get('genres', []))}\n"
        "*⟣────────────────────⟢*\n"
        f"*‣ Synopsis ⌯* *{synopsis}*\n\n"
        f"🔗*𝗢𝘂𝗿 𝗡𝗲𝘁𝘄𝗼𝗿𝗸* {NETWORK_TAG}"
    )


def p_cmd(update, context):
    if not context.args:
        update.message.reply_text("/p Movie Name | 2025")
        return

    raw = " ".join(context.args)
    if "|" in raw:
        title, year = [x.strip() for x in raw.split("|", 1)]
    else:
        title, year = raw, None

    tmdb = tmdb_search(title, year) or tmdb_search(title)
    if not tmdb:
        update.message.reply_text("❌ Not found")
        return

    tmdb.update(tmdb_details(tmdb["media_type"], tmdb["id"]))
    omdb = omdb_fetch(tmdb.get("imdb_id"))

    poster_path = tmdb.get("poster_path")
    if not poster_path:
        update.message.reply_text("Poster not available.")
        return

    update.message.reply_photo(
        photo=TMDB_IMG + poster_path,
        caption=format_caption(tmdb, omdb),
        parse_mode="Markdown"
    )


def main():
    # Required env checks
    if not BOT_TOKEN:
        raise RuntimeError("Missing BOT_TOKEN (set in Heroku Config Vars).")
    if not TMDB_API_KEY:
        raise RuntimeError("Missing TMDB_API_KEY (set in Heroku Config Vars).")
    if not APP_URL:
        raise RuntimeError("Missing APP_URL (set in Heroku Config Vars).")

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("p", p_cmd))

    port = int(os.environ.get("PORT", 5000))

    # Webhook secret path (better: use a separate secret, but token-path works)
    secret_path = BOT_TOKEN

    updater.start_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=secret_path,
        webhook_url=f"{APP_URL}/{secret_path}",
    )

    updater.idle()


print("✅ Bot running (Webhook)…")
main()
