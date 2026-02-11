
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------
# SECURITY SETTINGS
# -----------------------------------------------------------------------------

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# We fetch this from .env.prod or .env.test. Default is a dummy for local dev.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-dev-key')

# SECURITY WARNING: don't run with debug turned on in production!
# In Docker, we pass DEBUG=0 in .env.prod and DEBUG=1 in .env.test
DEBUG = int(os.environ.get('DEBUG', 1))

# ALLOWED_HOSTS
# Defines which domain names this Django instance will answer to.
# We pass a comma-separated string in the .env file (e.g., "api.example.co.uk,localhost")
if 'ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# -----------------------------------------------------------------------------
# APPLICATION DEFINITION
# -----------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'corsheaders',      # For Frontend connection
    'rest_framework',   # For API

    # Your Apps
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    # CORS must be here (Before CommonMiddleware)
    'corsheaders.middleware.CorsMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# -----------------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------------

# Logic: If in Docker (Postgres), use Env variables. 
# If on local (Laptop), use SQLite.

if os.environ.get('POSTGRES_DB'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'), # This matches service name 'db-prod'
            'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# -----------------------------------------------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# CSRF TRUSTED ORIGINS
# This tells Django: "Trust requests if the Host header matches these domains"
CSRF_TRUSTED_ORIGINS = [
    'http://api.nic-ball.co.uk',
    'https://api.nic-ball.co.uk',
    'http://test-api.nic-ball.co.uk',
    'https://test-api.nic-ball.co.uk',
]

# -----------------------------------------------------------------------------
# STATIC & MEDIA FILES (Served by Nginx in Prod)
# -----------------------------------------------------------------------------

# URL to access files in browser
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Where Python puts files when you run 'collectstatic'
# These match the volumes defined in docker-compose.yml
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')


# -----------------------------------------------------------------------------
# CORS (Cross-Origin Resource Sharing)
# -----------------------------------------------------------------------------

# Allowed origins for React Frontend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://portfolio.nic-ball.co.uk",
    "https://portfolio.nic-ball.co.uk",
    "http://nic-ball.co.uk",
    "https://nic-ball.co.uk",
]

# -----------------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -----------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------
# EMAIL CONFIGURATION (SMTP)
# -----------------------------------------------------------------------------

# If we have email settings in Env, use SMTP. Otherwise print to console.
if os.environ.get('EMAIL_HOST_USER'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')       # Gmail address
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') # App Password
    
    # Who the email comes FROM (Must match the authenticated user for Gmail)
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    
    # Who receives the contact form emails
    # We can use a separate env var, or just send it to yourself
    RECIPIENT_ADDRESS = os.environ.get('EMAIL_RECIPIENT', EMAIL_HOST_USER)
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
