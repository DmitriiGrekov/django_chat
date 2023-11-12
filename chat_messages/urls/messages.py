from django.urls import path

from chat_messages.views.messages import MessagesListView


urlpatterns = [
    path('<uuid:room_id>', MessagesListView.as_view(), name='list')
    
]
