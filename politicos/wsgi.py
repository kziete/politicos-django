"""
WSGI config for politicos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""


import os,sys

path = '/var/www/politicos'
if path not in sys.path:
    sys.path.insert(0, path) 


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "politicos.settings")

application = get_wsgi_application()
