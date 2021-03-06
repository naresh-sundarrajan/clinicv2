"""
Django settings for clinic project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.global_settings as DEFAULT_SETTINGS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    # ('CrazyGal', 'CrazyGal@example.com'),
)
MANAGERS = ADMINS


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!*=j)dku@2%e0#t$1ql6u+%8vjvzh(6x*mlb4xt^rg)49(x&h*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'user_sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'notetaker_1_0',
    'registration',
    'ckeditor',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'django_tables2',
    'django_filters',
	#including south for migrations    
	#'south',
    #Added Django-Bower 
    'djangobower',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'user_sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'two_factor.middleware.threadlocals.ThreadLocals',
)

#ADDED NEW DEPENDENCIES
BOWER_INSTALLED_APPS = (
    'jquery',
    'typeahead.js',
    'handlebars',
    'scriptjs',
    'form-autofill',
    'offCanvasMenu',
    'bootstrap-offcanvas',
)
    
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'clinic_1_0.urls'


WSGI_APPLICATION = 'clinic_1_0.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#bower_components
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR,'static')

#BOWER_STATIC_FILES_FINDER
#STATICFILES_FINDERS = (
#    'djangobower.finders.BowerFinder',
#)


# template location
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static","templates"),
)

AUTH_PROFILE_MODULE = 'notetaker_1_0.UserProfile'

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static","static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static","media")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static","static"),
        #os.path.join(os.path.dirname(BASE_DIR), "static","static-only/ckeditor"),
        )

CKEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(BASE_DIR), "static","media", "uploads")
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='localhost'
EMAIL_PORT=1025
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'
SITE_ID = 1

from django.core.urlresolvers import reverse_lazy
LOGOUT_URL = reverse_lazy('logout')
LOGIN_URL = reverse_lazy('two_factor:login')
LOGIN_REDIRECT_URL = reverse_lazy('two_factor:profile')

INTERNAL_IPS = ('127.0.0.1',)
  
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
  
TWO_FACTOR_CALL_GATEWAY = 'clinic_1_0.gateways.Messages'
TWO_FACTOR_SMS_GATEWAY = 'clinic_1_0.gateways.Messages'
  
SESSION_ENGINE = 'user_sessions.backends.db'
  
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
  
try:
    from .settings_private import *  # noqa
except ImportError as e:
    pass
