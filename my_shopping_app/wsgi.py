"""
WSGI config for my_shopping_app project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shopping_app.settings')

application = get_wsgi_application()
