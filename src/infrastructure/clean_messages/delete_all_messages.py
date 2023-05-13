import os

from src.settings import Config


def delete_all_messages():
    for files in os.listdir(Config.Paths.MESSAGES_DIR):
        if '.txt' in files:
            os.remove(Config.Paths.MESSAGES_DIR / files)
