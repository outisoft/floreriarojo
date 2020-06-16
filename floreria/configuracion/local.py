from .base import *
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'floreria',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}


STATICFILES_DIRS = (BASE_DIR,'static')
# url mediante el cual accedera a las imagenes subidas
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# ruta en donde quedan almacenados las imagenes
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
