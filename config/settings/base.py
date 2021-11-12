import os
import configparser
from decouple                               import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = ('config.backends.AuthBackend',)

# Application definition
INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # API - Apps
    'rest_framework',
    'rest_framework.authtoken',

    # Third Party Apps
    'django_countries',
    'crispy_forms',
    'bootstrap4',
    'django_user_agents',
    'dal',
    'dal_select2',
    "django_htmx",
    "corsheaders",

    # Project app
    'kapshop.apps.db.accounts',
    'kapshop.apps.db.addresses',
    'kapshop.apps.db.locations',
    'kapshop.apps.db.communications.emails',
    'kapshop.apps.db.kaps_admins',

    # accounting apps
    'kapshop.apps.db.accounting.banks',
    'kapshop.apps.db.accounting.coupons',
    'kapshop.apps.db.accounting.orderitems',
    'kapshop.apps.db.accounting.orders',
    'kapshop.apps.db.accounting.payments',

    #products apps
    'kapshop.apps.db.products.categories',
    'kapshop.apps.db.products.colors',
    'kapshop.apps.db.products.products',
    'kapshop.apps.db.products.sizes',
    'kapshop.apps.db.stores.stores',
    'kapshop.apps.db.stores.openinghours',

    # django admin must be below to let the model upload first
    'django.contrib.admin',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# DRF Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

LOGIN_REDIRECT_URL = '/login/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    #"corsheaders.middleware.CorsMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'kapshop/templates',)],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

CONFIG_DIR = os.path.join(BASE_DIR, 'config')
print('configuration path', CONFIG_DIR)

parser = configparser.ConfigParser()

parser.read_file(open(os.path.join(CONFIG_DIR, 'app.ini')))

# # gmail
EMAIL_BACKEND           = config('EMAIL_BACKEND')
EMAIL_HOST              = config('EMAIL_HOST')
EMAIL_PORT              = config('EMAIL_PORT')
EMAIL_HOST_USER         = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD     = config('EMAIL_PASSWORD')
EMAIL_USE_TLS           = config('EMAIL_USE_TLS')
EMAIL_SENDER            = config('EMAIL_SENDER')

# Password validation
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

# Internationalization
LANGUAGE_CODE   = 'en-us'

TIME_ZONE       = 'Africa/Johannesburg'

USE_I18N        = True

USE_L10N        = True

USE_TZ          = True

# Static files (CSS, JavaScript, Images)
BASE_PATH = os.path.join(BASE_DIR)

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'kapshop/static')]

STATIC_URL  = '/static/'

STATIC_ROOT = os.path.join(BASE_PATH, 'kapshop/static/includes')

MEDIA_URL   = '/media/'

MEDIA_ROOT  = os.path.join(BASE_PATH, 'kapshop/static/media')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'