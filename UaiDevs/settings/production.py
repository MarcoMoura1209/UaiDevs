from .base import *


DEBUG=False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

RATELIMIT_ENABLE = True


# Content Security Policy (CSP)
CSP_DEFAULT_SRC = ("'self'",)

CSP_SCRIPT_SRC = (
    "'self'",
    "https://code.iconify.design",
    "https://cdnjs.cloudflare.com",
)

CSP_STYLE_SRC = (
    "'self'",
    "https://cdnjs.cloudflare.com",
    "https://fonts.googleapis.com",
)

CSP_FONT_SRC = (
    "'self'",
    "https://fonts.gstatic.com",
    "https://cdnjs.cloudflare.com",
)

CSP_IMG_SRC = ("'self'",)

CSP_REPORT_ONLY = False


# Cross-site Scripting (XSS)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# SSL redirect 
SECURE_SSL_REDIRECT = True

#  HTTP Strict Transport Security (HSTS) 
SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Cross-site request forgery (CSRF) protection 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


LOGGING['handlers']['file'] = {
    'level': 'WARNING',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': '/var/log/django/core.log', # Lembre-se de dar permissão de escrita nesta pasta!
    'maxBytes': 1024 * 1024 * 15,
    'backupCount': 5,
    'formatter': 'verbose',
}

LOGGING['loggers']['django']['handlers'] = ['console', 'file']
LOGGING['loggers']['django']['level'] = 'WARNING'

LOGGING['loggers']['core']['handlers'] = ['console', 'file']
LOGGING['loggers']['core']['level'] = 'WARNING'