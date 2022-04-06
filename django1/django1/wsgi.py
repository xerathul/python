"""
외부서버하고 붙여쓸 때 사용 ex)아파치 톰캣
웹서버 기본적으로 제공
WSGI config for django1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')

application = get_wsgi_application()
