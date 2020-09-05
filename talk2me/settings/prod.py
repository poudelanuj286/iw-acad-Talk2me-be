from decouple import config
import dj_database_url
from .base import *


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://" + config('REACT_APP_API_URL'),
#     "https://" + config('REACT_APP_API_URL'),
# ]
CORS_ORIGIN_ALLOW_ALL = True # any website has access to my api