# Django settings for Airlines_L_A_F project.
import os
from pathlib import Path
from decouple import config

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k3_5@_wnpa#s2w1sh2rd%gn=oa@c7!qa_%u-js0q-2_@o$hskt'
DEBUG = config('DEBUG', cast=bool, default=True)

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = [
    '5ad9fdc6d07a41af8f1659085c779f63.vfs.cloud9.us-east-1.amazonaws.com',
    'air-env.eba-wj3sc457.us-east-1.elasticbeanstalk.com',
    '.elasticbeanstalk.com',
    '.amazonaws.com',
    'localhost',
    '127.0.0.1',
]

# CSRF_TRUSTED_ORIGINS: Specifies a list of trusted origins for safe CSRF handling.
CSRF_TRUSTED_ORIGINS = [
    'https://5ad9fdc6d07a41af8f1659085c779f63.vfs.cloud9.us-east-1.amazonaws.com',
    'https://air-env.eba-wj3sc457.us-east-1.elasticbeanstalk.com',
    'https://*.elasticbeanstalk.com',
    'https://*.amazonaws.com',
]

# Application definition
INSTALLED_APPS = [
    'spot_items',
    'registerer',
    'storages',
    'airport_staff',
    'crispy_bootstrap5',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# MIDDLEWARE: Hooks into Django's request/response processing.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

# ROOT_URLCONF: Root URL configuration module for the project.
ROOT_URLCONF = 'Airlines_L_A_F.urls'


# TEMPLATES: Configuration for template engine.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'spot_items/templates')],
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

WSGI_APPLICATION = 'Airlines_L_A_F.wsgi.application'

# DATABASES: Database configurations.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'geddam',
        'PASSWORD': os.environ['AIRLINES_DB_PASSWORD'],
        'HOST': 'laf-database-1.czc4ii6q8cs9.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# AUTH_PASSWORD_VALIDATORS: Password validation settings.
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

# Internationalization settings.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# settings for AWS s3 bucket and Static & Media Configuration for AWS S3 bucket.
AWS_STORAGE_BUCKET_NAME = 'myairlaf'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_LOCATION = 'media'
MEDIA_S3_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
MEDIA_URL = MEDIA_S3_URL
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
LOGIN_REDIRECT_URL = 'spot_items-home'
