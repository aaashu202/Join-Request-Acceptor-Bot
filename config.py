from os import environ

API_ID = int(environ.get("API_ID", "29640594"))
API_HASH = environ.get("API_HASH", "425945b03d2da856ab43e3f20e5570b7")
BOT_TOKEN = environ.get("BOT_TOKEN", "7741772339:AAFzv0ZqQ1o_BA-5VP0Sm8cLT9_De2DCqA8")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002242540576"))
ADMINS = int(environ.get("ADMINS", "6706180358 6710996831 999739828"))
DB_URI = environ.get("DB_URI", "mongodb+srv://awt:awt@cluster0.ltdwktu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "cluster0")
