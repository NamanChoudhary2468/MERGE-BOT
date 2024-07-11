import os


class Config(object):
    API_HASH = os.environ.get("1c2c6d7244d4576b2baab88337b1233a")
    BOT_TOKEN = os.environ.get("7098978512:AAHMV8j-r5YBSCryvWHIkMrE8vtNbbo7bxw")
    TELEGRAM_API = os.environ.get("25062134")
    OWNER = os.environ.get("6302921275")
    OWNER_USERNAME = os.environ.get("Spider_Man_02")
    PASSWORD = os.environ.get("namanplayz2468")
    DATABASE_URL = os.environ.get("mongodb+srv://File2Link:File2Link@cluster0.ygj9iuu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002208942976")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
