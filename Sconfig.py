#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5877458690:AAHu7GkMY7DX55mNuCIVh-q1vjjrbmuVWdo")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "26636879"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "28a083928b689da7dd0aceb67f04c65b")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQCPI_hM0aR3eBXRdzLD3dtkWGewaDuR1qvH_PjvaNCWlbcFrw-Te8ZGJaApItVK1qGbw9O4vOxG_B3CTOMgnXNxw_Yz7VqWxae8lhPCoAgNlB-l7O38nlUkk4icUiyEvRb5yb8AY4tTOGYhWw00RGIS3NfD1arrZ27GG8KKeMceua6ANWTbuWAVvtdgyZTRrLbk__ctxQcnlpWdoDpvHOFdWQYvglm7LQupeoSGLwTOMigkgmFvPl9Z26Q3ofRNe70BJlrGfE_UznNMBg8N-Cgfv8w0B8NqGeTOOhGe2qDzQFr6ikl-WoPTxEDEJeZkWqm4KiB5PJJtI0pK57McHiqEAAAAAWTHjb8A")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://AutoAnime:AutoAnime@autoanime.f8ahzhs.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
