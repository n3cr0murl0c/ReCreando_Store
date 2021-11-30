from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&t-&@$vg!pj4m@n#e-ee#wdi(b+1#zrssvch)n_1a55tx$so7h'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = MIDDLEWARE+[
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
INTERNAL_IPS = ("127.0.0.1","172.17.0.1")
try:
    from .local import *
except ImportError:
    pass
