import os
import importlib

async def load_modules(app):
    for file in os.listdir("bot/modules"):
        if file.endswith(".py"):
            module = f"bot.modules.{file[:-3]}"
            importlib.import_module(module)
