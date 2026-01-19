import subprocess
import os

def upload_to_drive(path, name):
    cmd = [
        "rclone", "copy",
        path,
        "gdrive:",
        "--progress"
    ]
    subprocess.run(cmd)
