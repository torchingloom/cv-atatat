
from config.settings_by_env.default import *

#STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static_root')
STATIC_ROOT = '/home/atlantij/webapps/cittavita_static'
#MEDIA_ROOT = '/home/atlantij/webapps/cittavita_static/media'
MEDIA_URL = '/static/media/'

#raise BaseException(MEDIA_ROOT)
#raise BaseException(__file__)

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % DATABASE_ENGINE, # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'atlantij_cittavita',                      # Or path to database file if using sqlite3.
        'USER': 'atlantij_cittavita',                      # Not used with sqlite3.
        'PASSWORD': 'b36b888c',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}