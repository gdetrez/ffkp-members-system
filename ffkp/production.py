from .settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ffkp_members',
        'USER': 'ffkp_members',
        'PASSWORD': 'axNuapFeld8',
        'HOST': '',
        'PORT': '',
    }
}
