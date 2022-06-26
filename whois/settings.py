"""
Django settings for whois project.

Generated by 'django-admin startproject' using Django 3.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pickle import TRUE
import dj_database_url
from pathlib import Path
from decouple import config
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',cast=bool)

ALLOWED_HOSTS = ["127.0.0.1","www.comparestupids.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'question',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'crispy_forms',

]

# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'




ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_UNIQUE_EMAIL=True
ACCOUNT_AUTHENTICATION_METHOD ="username_email"
ACCOUNT_EMAIL_VERIFICATION ='mandatory'
# ACCOUNT_USERNAME_REQUIRED=False
SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional'
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_AUTO_SIGNUP =True
SOCIALACCOUNT_LOGIN_ON_GET =False

LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL="/accounts/login/"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


# CRISPY_TEMPLATE_PACK = 'boostrap5'


#sending gmali email
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'nolanvenus33@gmail.com'
# EMAIL_HOST_PASSWORD = 'thegreatboy3@3'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#sending SES email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND  = 'django_ses.SESBackend'
EMAIL_HOST  = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = config('EMAIL_PORT',cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS',cast=bool)
DEFAULT_FROM_EMAIL=config('DEFAULT_FROM_EMAIL')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'whois.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

AUTHENTICATION_BACKENDS = [
     
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
     
]

WSGI_APPLICATION = 'whois.wsgi.application'

SITE_ID = 1
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES['default'] = dj_database_url.parse("postgres://shxwarcojinjch:48f0c4ebf0382b10e1bf62a1342b0b8c900c3c0cbaa2110fd70e339ef3d6b9de@ec2-54-164-40-66.compute-1.amazonaws.com:5432/dd1cbe9d6hqrqu")
 
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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
     
     
]

STATIC_ROOT = BASE_DIR / "static-root"

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
 
AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID=config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=config("AWS_STORAGE_BUCKET_NAME")
AWS_QUERYSTRING_AUTH=config("AWS_QUERYSTRING_AUTH",cast=bool)

LOGIN_URL = '/accounts/login/'

SECURE_SSL_REDIRECT = True


# if os.getcwd() == "/app":
#     SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')
#     SECURE_SSL_REQUIRED=True
#     DEBUG=False