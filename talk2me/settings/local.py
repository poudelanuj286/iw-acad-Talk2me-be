
from decouple import config, Csv
from .base import *

# DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME', default='talk2me'),
#         'USER': config('DB_USER', default='talk2me'),
#         'PASSWORD': config('DB_PASSWORD', default='talk2me'),
#         'HOST': config('DB_HOST', default='localhost')
#         }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}