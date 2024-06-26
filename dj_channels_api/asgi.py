"""
ASGI config for dj_channels_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from channel_app.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_channels_api.settings')
# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),
})
