"""
WSGI config for blog_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('~/Pulpit/django_girls') 
# os.environ["SECRET_KEY"] = '3#im4p5a#wy9b=(@f2%*q!x&*ceysfbiv#mvc8+!&5(da$9db%'
load_dotenv(os.path.join(project_folder, '.env'))
application = get_wsgi_application()
