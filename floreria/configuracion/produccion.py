# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

import dj_database_url
from decouple import config
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASES_URL')
    )
}
