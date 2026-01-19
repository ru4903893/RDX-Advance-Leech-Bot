import asyncio
import os
import subprocess

ARIA2_PORT = "6800"

def start_aria2():
    cmd = [
        "aria2c",
        "--enable-rpc",
        f"--rpc-listen-port={ARIA2_PORT}",
        "--rpc-listen-all=false",
        "--continue=true",
        "--max-connection-per-server=10",
        "--split=10",
        "--min-split-size=5M",
        "--file-allocation=trunc",
        "--log-level=notice"
    ]
    subprocess.Popen(cmd)

def aria2_available():
    return True
