import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(BASE_DIR)

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'fakester', 'static'),
]

ROOT_URLCONF = 'fakester.urls'
WSGI_APPLICATION = 'fakester.wsgi.application'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # fakester
    'redirects',
    'misc',

    # third party
    'bootstrap3',
    'ratelimit',
    'captcha',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'fakester', 'templates'),
        ],
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


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = True


LOGIN_URL = 'admin:login'
LOGIN_REDIRECT_URL = 'index'


#############################
# Third-party apps settings #
#############################

# django-bootstrap3
BOOTSTRAP3 = {
    'theme_url': 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/'
                 'paper/bootstrap.min.css',
    'include_jquery': True,
}

# django-recaptcha
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True


################
# Own settings #
################

# Local settings
try:
    from .local_settings import *
except ImportError:
    pass
