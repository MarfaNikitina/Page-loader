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
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'filename': '.page_loader_logging.log',
            'formatter': 'default_formatter',
        }
    },
    'loggers': {
        'logger_info': {
            'handlers': ['stream_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'logger_error': {
            'handlers': ['file_handler'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}


logging.config.dictConfig(LOGGING_CONFIG)
logger_info = logging.getLogger('logger_info')
logger_error = logging.getLogger('logger_error')
