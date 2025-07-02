"""
ASGI config for chatbot_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information, see:
https://channels.readthedocs.io/en/stable/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing  # make sure this file exists

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
