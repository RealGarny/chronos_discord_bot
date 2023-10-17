import os
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('BOT_TOKEN')

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters":{
        "verbose":{
            "format": "%(levelname)-10s - %(actime)s - %(module)-15s: %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers":{
        "console": {
            'level': "DEBUG",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "console2": {
            'level': "WARNING",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "console3": {
            'level': "INFO",
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w"
        },
    },
    "loggers":{
        "bot": {
            "handlers": ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ['console2', "console3"],
            "level": "INFO",
            "propagate": False
        },
    }
}

dictConfig(LOGGING_CONFIG)