from  .base import *
from .db import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 0

ALLOWED_HOSTS = ['djmarketrailway-production.up.railway.app']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = DB_POSTGRESQL