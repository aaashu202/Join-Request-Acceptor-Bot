from os import environ

API_ID = int(environ.get("API_ID", "29640594"))
API_HASH = environ.get("API_HASH", "425945b03d2da856ab43e3f20e5570b7")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002242540576"))
ADMINS = int(environ.get("ADMINS", "6710996831"))
DB_URI = environ.get("DB_URI", "mongodb+srv://worexe8487:e7JQljwBctv12sX2@cluster0.18clg.mongodb.net/?retryWrites=true&w=majority&appName=cluster0")
DB_NAME = environ.get("DB_NAME", "cluster0")
