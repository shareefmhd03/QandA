"""
Django settings for secondproject project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from django.contrib.messages import constants as messages




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m+$f1(@sj#if$m+&9ij$3#op@d%!)hhks$87@1%gxa8+8kn(3l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'channels',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'accounts',
    'posts',
    'profiles',
    'q_and_a.apps.QAndAConfig',
    'blog',
    'froala_editor',
    'storages',
    'tutorials',
    'admin_app',
    'allauth.socialaccount.providers.google',
    'challenges',
    'chat',
    
]

SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
]

AUTHENTICATION_BACKENDS = [
   
    'django.contrib.auth.backends.ModelBackend',  
    'allauth.account.auth_backends.AuthenticationBackend',
]

WEBPUSH_SETTINGS = {
   "VAPID_PUBLIC_KEY": "BCiUlB00zxInK-NMEy3qQ5N9Umpu1db_J8OkIFWOwWI1FE6aSknJilMuhTPBudF0kQ2pbc57g9-xffAYeruzhDM",
   "VAPID_PRIVATE_KEY": "nsaNzK-QRIf9YXWh8jQb8eD0mc8YFslu_OZqjdjhqDU",
   "VAPID_ADMIN_EMAIL": "shareef.mk03@gmail.com",
}

ROOT_URLCONF = 'secondproject.urls'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

# ASGI_APPLICATION = 'secondproject.asgi.application'
# ASGI_APPLICATION = 'secondproject.asgi.application'

ASGI_APPLICATION = 'secondproject.asgi.application'




DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'second',
       'USER': 'shareef',
       'PASSWORD': 'aezakmi',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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



AUTH_USER_MODEL = 'accounts.Accounts'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'second_project/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-error',
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'


CHANNEL_LAYERS = {
    'default': {
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
        # 'CONFIG': {
        #     'hosts': [('127.0.0.1', 6379)],
        # }
    }
}
