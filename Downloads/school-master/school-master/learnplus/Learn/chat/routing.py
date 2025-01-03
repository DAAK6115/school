from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(
        r"ws/instructor/messages/(?P<classe>\w+)/$", consumers.ChatConsumer.as_asgi()
    ),
    re_path(r"ws/student/messages/(?P<classe>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(
        r"ws/chat/private/(?P<user_id>\d+)/$", consumers.PrivateChatConsumer.as_asgi()
    ),
]
