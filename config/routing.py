from django.urls import re_path, path
from chat_messages.consumers.consumer import ChatConsumer

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns=[
    path('ws/messages/<uuid:room_id>/', ChatConsumer.as_asgi()),
    ]