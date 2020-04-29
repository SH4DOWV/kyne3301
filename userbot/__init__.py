""" Userbot initialization. """

import os

from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
from var import Var
load_dotenv("config.env")





os.system("pip install --upgrade pip")
if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)


CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)
""" PPE initialization. """

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

import pylast
from pySmartDL import SmartDL
from requests import get








# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.info("You MUST have a python version of at least 3.6."
              "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("TELEGRAM_API_KEY", None)
API_HASH = os.environ.get("TELEGRAM_API_HASH", None)

# Userbot Session String
STRING_SESSION = os.environ.get("TELEGRAM_STRING_SESSION", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Genius lyrics  API Token
GENIUS = os.environ.get("GENIUS_API_TOKEN", None)
GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)



# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_PROTECTOR", "True"))




# Heroku Credentials for updater.
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
HEROKU_API_KEY = os.environ.get("HEROKU_APIKEY", None)


UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/rekcah-pavi/javes")
    

TELEGRAPH_SHORT_NAME = os.environ.get(
   "TELEGRAPH_SHORT_NAME", 
   "Javes")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)



# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
PM_MESSAGE = os.environ.get(f"PM_MESSAGE", None)
JAVES_NAME = os.environ.get("JAVES_NAME", None)
# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Default .alive name
ALIVE_NAME = os.environ.get("YOUR_SHORT_NAME", None)

BLOCK_MESSAGE = os.environ.get("BLOCK_MESSAGE", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

from userbot import ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
from userbot import DEFAULTUSER



KYNE_MSG = (
   f"kyne ")
   
ORI_MSG = (
   f"Hello Sir, I can't allow you to {ALIVE_NAME}'s PM without his permissions please be patient, Thankyou ")
   
BLOCK_MSG = (
   f"I am not going to allow you to spam {DEFAULTUSER}'s PM, You have been blocked ")
   
   

KYNE_NNAME = str(KYNE_NAME) if KYNE_NAME else str(KYNE_MSG)
AFK_MSG = (
   f"Hello Sir, {DEFAULTUSER} is offline Just leave Your message, Thankyou!")

AFK_MESSAGE = os.environ.get("AFK_MESSAGE", None)

ALIVE_S_MESSAGE = os.environ.get("ALIVE_S_MESSAGE", None)
BIO_MESSAGE = os.environ.get("BIO_MESSAGE", None)
ALIVE_E_MESSAGE = os.environ.get("ALIVE_E_MESSAGE", None)

BIO_MSG = (
   f"")

ALIVE_S_MSG = (
   f"kyne mode on!")

ALIVE_E_MSG = (
   f"Databases functioning normally!! ")


# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION),
                         API_KEY,
                         API_HASH,
                         connection_retries=None,
                         auto_reconnect=False,
                         lang_code='en')
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot",
                         API_KEY,
                         API_HASH,
                         connection_retries=None,
                         auto_reconnect=False,
                         lang_code='en')


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if not entity.creator:
        if entity.default_banned_rights.send_messages:
            LOGS.info(
                "Your account doesn't have rights to send messages to BOTLOG_CHATID "
                "group. Check if you typed the Chat ID correctly.")
            quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
