from .base                                                      import *


DEBUG  = True#not bool(config("DEBUG"))

IS_ENV = 'DEV'

ALLOWED_HOSTS = [ 'localhost', '127.0.0.1', ]

INSTALLED_APPS += [ 'debug_toolbar', ]

MIDDLEWARE += [ 'debug_toolbar.middleware.DebugToolbarMiddleware', ]

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql',
        'NAME'      : config("KAPS_DB_NAME"),
        'USER'      : config("KAPS_DB_USER"),
        'PASSWORD'  : config("KAPS_DB_PASSWORD"),
        'HOST'      : config("KAPS_DB_HOST"),
        'PORT'      : config("KAPS_DB_PORT"),
    }
}

# DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS'   : False,
    'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
}

print("\n")
print("DEBUG        = ", DEBUG)
print("DATABASES    = ", DATABASES['default']['NAME'])
print("HOST         = ", DATABASES['default']['HOST'])
print("TEMPLATES    = ", TEMPLATES[0]['DIRS'])
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT)