# backend/kittygram_backend/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY и DEBUG читаем из .env
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG      = os.environ.get('DEBUG', 'False') == 'True'

# В продакшене подставьте сюда свой хост (или через ALLOWED_HOSTS в .env)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'djoser',
    'cats.apps.CatsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kittygram_backend.urls'

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

WSGI_APPLICATION = 'kittygram_backend.wsgi.application'

# Подключаем PostgreSQL из переменных окружения
if 'POSTGRES_DB' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql',
            'NAME':     os.environ['POSTGRES_DB'],
            'USER':     os.environ['POSTGRES_USER'],
            'PASSWORD': os.environ['POSTGRES_PASSWORD'],
            'HOST':     os.environ.get('DB_HOST', 'db'),
            'PORT':     os.environ.get('DB_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# В продакшене обязательно настроить локаль и таймзону
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# Статика и медиа
# URL‑префиксы — должны соответствовать proxy в nginx
STATIC_URL  = '/kittygram/static/'
MEDIA_URL   = '/kittygram/media/'

# Куда django collectstatic собирает все файлы
STATIC_ROOT = BASE_DIR / 'static'
# Куда django сохраняет загружённые пользователями файлы
MEDIA_ROOT  = BASE_DIR / 'media'

# Остальные настройки
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', 
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

