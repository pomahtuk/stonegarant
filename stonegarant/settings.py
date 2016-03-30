# Django settings for stonegarant project.

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

#DEBUG = False if (os.environ.get('DJANGO_DEBUG') and os.environ.get('DJANGO_DEBUG') is False) else True
# just for stage
DEBUG = True
FORCE_WWW = not DEBUG

ADMINS = (
    ('PMaN', 'pman89@ya.ru'),
)

MANAGERS = ADMINS

import urlparse

# Register database schemes in URLs.
urlparse.uses_netloc.append('mysql')

try:

    # Check to make sure DATABASES is set in settings.py file.
    # If not default to {}

    if 'DATABASES' not in locals():
        DATABASES = {}

    if 'DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])

        # Ensure default database exists.
        DATABASES['default'] = DATABASES.get('default', {})

        # Update with environment configuration.
        DATABASES['default'].update({
            'ENGINE': 'django.db.backends.mysql',
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        })

    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'stonegarant',       # Or path to database file if using sqlite3.
                'USER': 'root',               # Not used with sqlite3.
                'PASSWORD': '',                  # Not used with sqlite3.
                'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            }
        }

except Exception:
    print 'Unexpected error:', sys.exc_info()


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'stonegarant', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b1m^i+3*w8x5z)5nxx71%v-bq3rgk683yxp^+rk#s4zm=ch-i&amp;'

# List of callables that know how to import templates from various sources.
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(PROJECT_ROOT, 'template')],
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.csrf',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
            'stonegarant.context_processors.jivosite',
        ],
        'loaders': [
            ('django.template.loaders.cached.Loader', [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]),
        ],
    },
}]

MIDDLEWARE_CLASSES = (
    'stonegarant.middleware.HostnameRedirectMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'stonegarant.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'stonegarant.wsgi.application'


THUMBNAIL_CHECK_CACHE_MISS = True

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (80, 80), 'crop': True},
        'preview': {'size': (60, 80), 'crop': False, 'autocrop': True},
        'product': {'size': (375, 480), 'crop': False, 'autocrop': True},
        'thumb': {'size': (160, 160), 'crop': False, 'autocrop': True},
        'catalog': {'size': (230, 320), 'crop': False, 'autocrop': True},
        'email': {'size': (230, 250), 'crop': False, 'autocrop': True},
        'work': {'size': (200, 280), 'crop': False},
        'ready': {'size': (400, 560), 'crop': False},
        'admin': {'size': (100, 100), 'crop': False}
    },
}

THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')  # enter your secret access key
AWS_STORAGE_BUCKET_NAME = 'stonegarant'
AWS_IS_GZIPPED = True

AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}

STATICFILES_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_STORAGE = 'stonegarant.storage.CachedS3BotoStorage'

S3_URL = 'http://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL + '/'
MEDIA_URL = S3_URL + '/media/'
COMPRESS_URL = STATIC_URL

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/x-javascript', 'stonegarant.compilers.JSXCompiler'),
)

GZIP_CONTENT_TYPES = (
    'text/css',
    'application/javascript',
    'application/x-javascript',
    'text/javascript'
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Stonegarant Admin'
}

INSTALLED_APPS = (
    'suit',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'easy_thumbnails',
    'debug_toolbar',
    'suit_redactor',
    'pagination',
    'storages',
    'gunicorn',
    'uuslug',
    'stonegarant',
    'compressor',
    'django_premailer'
)

EMAIL_USE_SSL = True
EMAIL_HOST = os.environ.get('YANDEX_HOST')
EMAIL_HOST_USER = os.environ.get('YANDEX_USER')
EMAIL_HOST_PASSWORD = os.environ.get('YANDEX_PASSWORD')
EMAIL_PORT = os.environ.get('YANDEX_PORT')

JIVOSITE_ID = os.environ.get('JIVOSITE_ID', 'd5VtEOvH6q')


DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
    'INTERCEPT_REDIRECTS': False,
    'MEDIA_URL': '/__debug__/m/',
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'stonegarant_cache',
#     }
# }


# CACHES = {
#     'default': {
#         'BACKEND': 'django_bmemcached.memcached.BMemcached',
#         'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
#         'OPTIONS': {
#                     'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
#                     'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
#             }
#     }
# }

os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

CACHES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

        # Use binary memcache protocol (needed for authentication)
        'BINARY': True,

        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,

        'OPTIONS': {
            # Enable faster IO
            'no_block': True,
            'tcp_nodelay': True,

            # Keep connection alive
            'tcp_keepalive': True,

            # Timeout for set/get requests
            '_poll_timeout': 2000,

            # Use consistent hashing for failover
            'ketama': True,

            # Configure failover timings
            'connect_timeout': 2000,
            'remove_failed': 4,
            'retry_timeout': 2,
            'dead_timeout': 10
        }
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
