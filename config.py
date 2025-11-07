from os import environ

class Config:
    API_ID = int(environ.get("API_ID", "23903140"))
    API_HASH = environ.get("API_HASH", "579f1bcf3eac1660d81ef34b09906012")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7697009107:AAFXeFf23RviLPSc__Hdi9Nw7kqHzFgre0U") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot")
    DATABASE_URI = environ.get("DATABASE_URI", " ")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER = int(environ.get("BOT_OWNER", "6317211079"))
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

