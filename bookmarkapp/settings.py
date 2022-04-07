''' to enable .env work '''
from decouple import config,Csv

''' import os for os modules ''' 
import os


INTERNAL_IPS = ['127.0.0.1']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    # django apps 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
     # third party apps                                                                                                                                                                                                
    'widget_tweaks',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'debug_toolbar',
    'admin_honeypot',
    
      # local 
    'bookmark.apps.BookmarkConfig',
    'books.apps.BooksConfig',
    'orders.apps.OrdersConfig',
    
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'bookmarkapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bookmarkapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

''' django default path for static files '''
STATIC_URL = '/static/'

''' which defines the location of static files in local development '''
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/'),]

''' STATIC_ROOT 121 is the location of static files for production so it must be set to a different name, typically staticfiles . '''
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# ''' STATICFILES_FINDERS 123 which tells Django how to look for static file directories. '''

# STATICFILES_FINDERS = [
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder'
# ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


''' use CustomUser instead of the default User model. '''
AUTH_USER_MODEL = 'bookmark.CustomUser'

''' login redirect '''
LOGIN_REDIRECT_URL = 'bookmark:home'

''' logout redirect '''
ACCOUNT_LOGOUT_REDIRECT_URL = 'bookmark:home'

''' signup redirect '''
SIGNUP_REDIRECT_URL = 'bookmark:home'

''' ask for password once '''
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

''' Email login alone configuration '''
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True # 
ACCOUNT_UNIQUE_EMAIL = True

''' django custom form decoration '''
CRISPY_TEMPLATE_PACK = 'bootstrap4'

''' custom authentication using allauth '''
''' django-allauth config '''
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

DEFAULT_FROM_EMAIL = 'admin@codinggee.com'
''' The EMAIL_BACKEND setting indicates the class to use to send emails '''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STRIPE_TEST_PUBLISHABLE_KEY=config('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY=config('STRIPE_TEST_SECRET_KEY')

''' cache config '''
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')
''' Security is a major concern for any website '''
# if ENVIRONMENT == 'development':
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600 # new
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new
SECURE_HSTS_PRELOAD = True # new
SECURE_CONTENT_TYPE_NOSNIFF = True # new
SECURE_REFERRER_POLICY = 'no-referrer'

''' Heroku '''
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

import django_heroku
django_heroku.settings(locals())