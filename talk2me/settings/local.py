from decouple import config, Csv
import dj_database_url

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DEBUG = config('DEBUG', cast=bool)

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