
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secondproject.settings')
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import django
from chat import routing



django.setup()
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})




