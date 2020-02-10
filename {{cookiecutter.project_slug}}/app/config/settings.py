# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']

DEBUG = True if os.getenv('DJANGO_DEBUG') == 'true' else False

# region apps

APPS_DJANGO = (
    # pre-django
    'flat_responsive',  # Mobile support for flat theme
    'flat',  # Admin flat theme
    'colorfield',  # colorpicker field for admin

    # core
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
)

APPS_CORE = (
    'core',
    'pages',
    'blog',
)

APPS_WAGTAIL = (
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.settings',
    'wagtail.contrib.wagtailsitemaps',
    'wagtail.contrib.table_block',

)

if DEBUG:
    APPS_WAGTAIL += (
        'wagtail.contrib.wagtailstyleguide',
    )

APPS_DJANGO_PLUGINS = (
    'django_extensions',
    'django_markup',
    'meta',
    'wagtailmetadata',
    'modelcluster',
    'taggit',
    'honeypot',
    'overextends',
    'widget_tweaks',
    'analytical',
    'svg_templatetag',  # adds template tag to inline SVGs
)

if DEBUG:
    APPS_DJANGO_PLUGINS += (
        'debug_toolbar',  # Development only!
    )

INSTALLED_APPS = APPS_DJANGO + APPS_CORE + APPS_WAGTAIL + APPS_DJANGO_PLUGINS

# endregion

# region Middleware

MIDDLEWARE_CLASSES = (

    # Django
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Wagtail
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    # Honeypot
    'honeypot.middleware.HoneypotMiddleware'

)

if DEBUG:
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',  # Debug toolbar
    )

# endregion

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Django
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Wagtail
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# region Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DJANGO_DB_NAME'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST'),
        'PORT': os.getenv('DJANGO_DB_PORT'),
    }
}

# endregion

# region Authentication

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',
)

# endregion

# region Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# endregion

# region File Storage

# The URL used to serve the media files in MEDIA_ROOT directory
MEDIA_URL = os.getenv('DJANGO_MEDIA_URL', '/media/')
# Absolute filesystem path to the directory that will hold user-uploaded files. Used by FileSystemStorage.
MEDIA_ROOT = os.getenv('DJANGO_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
# The URL used to serve the static files in STATIC_ROOT directory
STATIC_URL = os.getenv('DJANGO_STATIC_URL', '/static/')
# Absolute filesystem path to the directory that will hold collectstatic files. Used by StaticFilesStorage.
STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', os.path.join(BASE_DIR, 'static_collected'))

STATICFILES_STORAGE = os.getenv('DJANGO_STATICFILES_STORAGE', 'django.contrib.staticfiles.storage.StaticFilesStorage')
# Class to be used for any file-related operations that don’t specify a particular storage system
DEFAULT_FILE_STORAGE = os.getenv('DJANGO_DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# endregion

# region Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST')
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = os.getenv('DJANGO_DEFAULT_FROM_EMAIL')

# endregion

# region Sites

SITE_ID = 1

# endregion

# region Misc

INTERNAL_IPS = []

if DEBUG:
    INTERNAL_IPS += [
        '127.0.0.1',  # Localhost
        '172.20.0.1',  # Docker
        '192.168.99.1'  # Docker in VirtualBox
    ]

# Nuclear option for toolbar to show no matter what
# def show_toolbar(request):
#     return True
#
#
# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK": show_toolbar,
# }
# endregion

# region django-storages
AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = os.getenv('DJANGO_AWS_S3_REGION_NAME')
AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=0' if DEBUG else 'max-age=86400', }
AWS_IS_GZIPPED = True
GZIP_CONTENT_TYPES = (
    'text/plain',
    'text/xml',
    'text/css',
    'text/javascript',
    'application/xml',
    'application/rss+xml',
    'application/xhtml+xml',
    'application/javascript',
    'application/x-javascript',
    'image/svg+xml',
)
AWS_QUERYSTRING_AUTH = False
AWS_AUTO_CREATE_BUCKET = True
# endregion

# region Wagtail
WAGTAIL_SITE_NAME = os.getenv('DJANGO_PROJECT_NAME')
BLOG_PAGINATION_PER_PAGE = 3
# endregion

# region django-meta
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True
META_SITE_NAME = os.getenv('DJANGO_PROJECT_NAME')
# endregion

# region honeypot
HONEYPOT_FIELD_NAME = os.getenv('DJANGO_HONEYPOT_FIELD_NAME')
# endregion

# region typekit
# TYPEKIT_ID = None
# endregion

# region django-analytical
# GOOGLE_ANALYTICS_PROPERTY_ID = os.getenv('GOOGLE_ANALYTICS_PROPERTY_ID')
# GOOGLE_ANALYTICS_SITE_SPEED = True
# endregion
