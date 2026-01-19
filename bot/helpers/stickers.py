"""
CandyCloud Sticker Collection 🍭
Safe & public Telegram stickers
"""

STICKERS = {
    # General
    "start": "CAACAgUAAxkBAAEKZQ9lJH3zN8qJqkSgAAE1oXyQ1lKQ2gACdAQAAv4sCFW3v5oYkQABHgQ",
    "help": "CAACAgUAAxkBAAEKZRJm1wABpEw4b3V4qfM2AAH6ZQ2XbZ3RAAIbAQACjzZAVc8m2nUEAAEeBA",

    # Actions
    "mirror": "CAACAgUAAxkBAAEKZRBj3lUAAaYkP3fQ5mYAAQABnXr9u2dXo3IAAhYBAAKG9UoV2p0XoQABHgQ",
    "leech": "CAACAgUAAxkBAAEKZRNm2QABPp3gAAGy9qM2AAHk5Q4Yp3wAAh8BAAKG9UoVtX2KkAEeBA",

    # Status
    "downloading": "CAACAgUAAxkBAAEKZRZm3QABK4xU2p9tAAH6XQ3a2xYRAAIQAQACjzZAVeY9xj8eBA",
    "uploading": "CAACAgUAAxkBAAEKZRpntwAB1lQAAZy4QAAH7kQ4nAAEOAAIbAQACjzZAVQAB9b9cHgQ",

    # Result
    "success": "CAACAgUAAxkBAAEKZRxm4AABV6PAAAGjAAHn5Q4Ff4AIAAIWAQACjzZAVe0qF44eBA",
    "error": "CAACAgUAAxkBAAEKZR5m4gABP0wAAZ2YAAH7lQ4Ff4AIAAIUAQACjzZAVYtq9pMeBA"
}


def get_sticker(name: str):
    """
    Safely get sticker by name
    """
    return STICKERS.get(name, STICKERS["start"])
