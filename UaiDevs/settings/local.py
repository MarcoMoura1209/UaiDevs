from .base import *


DEBUG=True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

RATELIMIT_ENABLE = False


LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['core']['level'] = 'DEBUG'

LOGGING['loggers']['django.db.backends'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}
