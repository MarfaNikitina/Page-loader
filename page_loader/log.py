# import logging
import logging.config
# from logging import StreamHandler, Formatter
# import sys


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default_formatter': {
            'format': '[%(asctime)s: %(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler', 
            'formatter': 'default_formatter',
        },
    },
    'loggers': {
        'logger': {
            'handlers': ['stream_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('logger')
