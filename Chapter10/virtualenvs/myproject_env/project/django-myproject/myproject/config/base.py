"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, sys

from auth_extra.password_validation import (
    SpecialCharacterInclusionValidator)
from utils.misc import get_media_svn_revision, get_git_changeset


USE_DJANGO_CRISPY_FORMS = False
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Build paths inside the project like this:
# os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))

EXTERNAL_BASE = os.path.join(BASE_DIR, "externals")
EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, "libs")
EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, "apps")
sys.path = ["", EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c!19961!voix0tt82=9by*uq5=2&9+&(cl)ogv-#t_)8l2s&y)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.forms',
    'crispy_forms',
    'haystack',
    'sorl.thumbnail',
    'watermarker',
    'social_django',
    'cms',
    'menus',
    'treebeard',
    'djangocms_admin_style',
    'sekizai',
    'mptt',
    'django_mptt_admin',
    'tastypie',
    'rest_framework',
    # local apps
    'artists',
    'bulletin_board',
    'cms_extensions',
    'custom_admin',
    'cv',
    'editorial',
    'email_messages',
    'external_auth',
    'ideas',
    'likes',
    'locations',
    'magazine',
    'movies',
    'music',
    'quotes',
    'products',
    'search',
    'utils',
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]
MIDDLEWARE_CLASSES = MIDDLEWARE

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

CMS_TEMPLATES = (
    ("cms/default.html", _("Default")),
    ("cms/magazine.html", _("Magazine")),
    ("cms/start.html", _("Homepage")),
)

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
        'OPTIONS': {
            'max_similarity': 0.5,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
    {
        'NAME': 'auth_extra.password_validation.'
                'MaximumLengthValidator',
        'OPTIONS': {
            'max_length': 32,
        },
    },
    {
        'NAME': 'auth_extra.password_validation.'
                'SpecialCharacterInclusionValidator',
        'OPTIONS': {
            'special_chars': ('{', '}', '^', '&') +
                             SpecialCharacterInclusionValidator.
                                 DEFAULT_SPECIAL_CHARACTERS
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# - if using SVN:
# STATIC_URL = f'/static/{get_media_svn_revision(BASE_DIR)}/'
# - if using GIT:
# STATIC_URL = f'/static/{get_git_changeset(BASE_DIR)}/'
# - otherwise:
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'site_static'),
]

UPLOAD_URL = f'{MEDIA_URL}upload/'
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'upload')

FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'tmp')

CACHES = {
    'memcached': {
        'BACKEND': 'django.core.cache.backends.'
                   'memcached.MemcachedCache',
        'LOCATION': os.environ.get('CACHE_LOCATION',
                                   '127.0.0.1:11211'),
        "TIMEOUT": 60, # 1 minute
        "KEY_PREFIX": os.environ.get('CACHE_KEY',
                                     'myproject_production'),
    },
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('CACHE_LOCATION',
                                   'redis://127.0.0.1:6379/1'),
        "TIMEOUT": 60, # 1 minute
        "KEY_PREFIX": os.environ.get('CACHE_KEY',
                                     'myproject_production'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        },
    },
}
CACHES['default'] = CACHES['memcached']
# or
# CACHES['default'] = CACHES['redis']