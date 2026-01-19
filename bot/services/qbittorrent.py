import os
import subprocess

def start_qb():
    subprocess.Popen([
        "qbittorrent-nox",
        "--webui-port=8080"
    ])

def is_available():
    return not bool(os.getenv("DYNO"))  # Heroku check

