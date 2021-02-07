from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from ws.connect import ConnectConsumer
from django.urls import re_path


websocket_urlpatterns = [
    re_path(r'connect/$', ConnectConsumer.as_asgi()),
]

application = ProtocolTypeRouter({

        'websocket': AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        ), 
})