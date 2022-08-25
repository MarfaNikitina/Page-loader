import logging
import logging.config
from logging import StreamHandler, Formatter
import sys


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default_formatter': {
            'format': '[%(asctime)s: %(levelname)s] %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler', 
            'formatter': 'default_formatter',
        },
    },
    'loggers': {
        'debug_logger': {
            'handlers': ['stream_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('debug_logger')
logger.debug('debug log')




# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# handler = StreamHandler(stream=sys.stdout)
# logger.addHandler(handler)
# handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
# logger.debug('debug information')

