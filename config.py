from os import getenv
from STORMDB.data import STORMS

API_ID = int(getenv("API_ID", "25981592"))
API_HASH = getenv("API_HASH", "709f3c9d34d83873d3c7e76cdd75b866")
SESSION1 = getenv("SESSION")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/b99ed1fb1efd15e38389c.png")
HELP_PIC = getenv("HELP_PIC", "https://telegra.ph/file/84a4e224562ad2dd1a6ad.png")
OWNER_ID = int(getenv("OWNER_ID", "5473771943"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
OPENAIKEY = getenv("OPENAIKEY")
MURL = getenv("MANGO_URL")
PM_PIC = "https://telegra.ph/file/b99ed1fb1efd15e38389c.png"
SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")

SUDOS = getenv("SUDO_USERS", None)
SUDO_USERS = []
if SUDOS:
    sudos = str(SUDOS).split(" ")
    for sudo_id in sudos:
        SUDO_USERS.append(int(sudo_id))
SUDO_USERS.append(OWNER_ID)
for x in STORMS:
    SUDO_USERS.append(x)

SESSIONS = [SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10]
