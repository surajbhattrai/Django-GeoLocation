from pathlib import Path
from decouple import config
import os
from django import conf

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "asfasfaf0283r2hjsa"
DEBUG = True
ALLOWED_HOSTS = ['194.195.118.42', '127.0.0.1', 'djangofoodonline.com', 'www.djangofoodonline.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'vendor',
    'menu',
    'marketplace',
    'customers',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'orders.request_object.RequestObjectMiddleware', 
]

ROOT_URLCONF = 'foodOnline_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.get_vendor',
                # 'accounts.context_processors.get_google_api',
                'marketplace.context_processors.get_cart_counter',
                'marketplace.context_processors.get_cart_amounts',
                'accounts.context_processors.get_user_profile',
                # 'accounts.context_processors.get_paypal_client_id',
            ],
        },
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',                   
    }
}

WSGI_APPLICATION = 'foodOnline_main.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'
AUTH_PASSWORD_VALIDATORS = []



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True



STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
    'foodOnline_main/static'
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Email configuration
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'foodOnline Marketplace <django.foodonline@gmail.com>'
# PAYPAL_CLIENT_ID = config('PAYPAL_CLIENT_ID')
# SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'
# RZP_KEY_ID = config('RZP_KEY_ID')
# RZP_KEY_SECRET = config('RZP_KEY_SECRET')