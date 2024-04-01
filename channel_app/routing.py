from django.urls import path

from .consumer import MyAsyncConsumer, MySyncConsumer

websocket_urlpatterns = [
    path('ws/sc/', MySyncConsumer.as_asgi(), name='sc_ws'),
    path('ws/ac/', MyAsyncConsumer.as_asgi(), name='ac_ws'),
]
