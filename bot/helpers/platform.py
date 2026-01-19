import os

def is_heroku():
    return bool(os.getenv("DYNO"))
