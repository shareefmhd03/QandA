from . consumers import ChatConsumer
from django.urls import path

websocket_urlpatterns=[
    path('chat/',ChatConsumer.as_asgi()),
]

