from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).absolute().parent.parent
    MESSAGES_DIR = BASE_DIR / 'messages'

    SERVER_HOST = 'localhost'
    SERVER_PORT = 8000
