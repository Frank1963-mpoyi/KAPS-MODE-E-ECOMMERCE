import dj_database_url

from .base                                                  import *

DEBUG               =  bool(config("DEBUG"))

IS_ENV = 'PROD'

ALLOWED_HOSTS       = ['127.0.0.1', 'kapembu-seraphin.herokuapp.com']

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Honor the 'X-Forwarded-Proto' header fro request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# #Done with postgresql
DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql',
        'NAME'      : parser.get('kapshop_dev', 'KAPS_DB_NAME'),
        'USER'      : parser.get('kapshop_dev', 'KAPS_DB_USER'),
        'PASSWORD'  : parser.get('kapshop_dev', 'KAPS_DB_PASSWORD'),
        'HOST'      : parser.get('kapshop_dev', 'KAPS_DB_HOST') or '127.0.0.1',
        'PORT'      : parser.getint('kapshop_dev', 'KAPS_DB_PORT') or '5432',

    }
}

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


# Static files (CSS, JavaScript, Images)
BASE_PATH = os.path.join(BASE_DIR)

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'kapshop/static')]

STATIC_URL  = '/static/'

STATIC_ROOT = os.path.join(BASE_PATH, 'kapshop/static/includes')

MEDIA_URL   = '/media/'

MEDIA_ROOT  = os.path.join(BASE_PATH, 'kapshop/static/media')

STATICFILES_STORAGE     = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ENVIRONMENT = 'PRODUCTION'

print("\n")
print("DEBUG        = ", DEBUG      )
print("MODE         = ", ENVIRONMENT)
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT )
print("\n")