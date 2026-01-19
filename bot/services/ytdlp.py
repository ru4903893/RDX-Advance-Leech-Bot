import subprocess
import os

def ytdlp_download(url, out):
    subprocess.run([
        "yt-dlp",
        "-o", f"{out}/%(title)s.%(ext)s",
        url
    ])
