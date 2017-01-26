#!/usr/bin/env python
# coding: utf-8

import environ
import os
import dj_database_url
try:
    from django.urls import reverse_lazy
except:
    from django.core.urlresolvers import reverse_lazy

env = environ.Env()
# env.read_env()


ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('associados')
BASEDIR = APPS_DIR
print(ROOT_DIR)
print(BASEDIR)

DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
#TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Marcos Daniel Petry', 'marcospetry@gmail.com'),
    # ('Valder Gallo', 'valdergallo@gmail.com'),
    ('Osvaldo Santana Neto', 'osantana@python.org.br'),
    # ('Carlos Leite', 'carlos.leite@znc.com.br'),
)
MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}


# Miscelaneous
APPEND_SLASH = True
SITE_ID = 1
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# i18n & l10n
USE_I18N = True
USE_L10N = True

USE_THOUSAND_SEPARATOR = True
LANGUAGES = [
    ('pt-BR', 'Portuguese Brazil')
]
LANGUAGE_CODE = 'pt-BR'
DEFAULT_LANGUAGE = 1
#LOCALE_PATHS = (
#    os.path.join(BASEDIR, "locale"),
#)

USE_TZ = True
TIME_ZONE = 'America/Sao_Paulo'


# Media & Static
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = "static"

AWS_ACCESS_KEY_ID = os.environ.get('BUCKET_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('BUCKET_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
AWS_REGION_BUCKET_NAME = os.environ.get("BUCKET_REGION")

# MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_ROOT = str(ROOT_DIR.path('media'))
MEDIA_URL = '//%s.%s.amazonaws.com/media/' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION_BUCKET_NAME)
# STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_ROOT = str(ROOT_DIR.path('static'))
STATIC_URL = '//%s.%s.amazonaws.com/static/' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION_BUCKET_NAME)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Security
SECRET_KEY = 'yc!+ii!psza0mi)&amp;vnn_rdsip5ipdyr(0w8hjllxw6p)!wgo1e'
LOGIN_URL = '/'
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('members-dashboard')
AUTHENTICATION_BACKENDS = (
    'associados.authemail.backends.EmailBackend',
)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

MIGRATION_MODULES = {
    'municipios': 'associados.municipios.migrations'
}

# Apps
INSTALLED_APPS = (
    #apps
    # '',
    'associados.members',
    'associados.payment',
    'associados.core',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',

    #extra
    'bootstrap_toolkit',
    'pipeline',
    'django_extensions',
    'sorl.thumbnail',
    'django_gravatar',
    'municipios',

)


# Logging
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Email
EMAIL_HOST_USER = os.getenv('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# System contact email address
DEFAULT_FROM_EMAIL = "contato@python.org.br"
EMAIL_CONTACT_ADDRESS = DEFAULT_FROM_EMAIL

# 3rd party applications
PAGSEGURO = {
    'email': os.environ.get('PAGSEGURO_EMAIL'),
    'charset': 'UTF-8',
    'token': os.environ.get('PAGSEGURO_TOKEN'),
    'currency': 'BRL',
    'itemId1': '0001',
    'itemQuantity1': 1,
}

PAGSEGURO_BASE = 'https://ws.pagseguro.uol.com.br/v2'
PAGSEGURO_CHECKOUT = '%s/checkout' % PAGSEGURO_BASE
PAGSEGURO_TRANSACTIONS = '%s/transactions' % PAGSEGURO_BASE
PAGSEGURO_TRANSACTIONS_NOTIFICATIONS = '%s/notifications' % PAGSEGURO_TRANSACTIONS
PAGSEGURO_WEBCHECKOUT = 'https://pagseguro.uol.com.br/v2/checkout/payment.html?code='
PAGSEGURO_PRE_APPROVAL = '%s/pre-approvals/request' % PAGSEGURO_BASE
PAGSEGURO_WEB_PRE_APPROVAL = 'https://pagseguro.uol.com.br/v2/pre-approval/request.html?code='

GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')
GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')

DSN = os.getenv("DJANGO_DSN")
if DSN:
    RAVEN_CONFIG = {'dsn': DSN}
    INSTALLED_APPS = INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',
    )


PIPELINE = {

}

# # Local settings
# try:
#     exec(open('associados/settings_local.py').read())
# except IOError:
#     pass
