from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView

from core.views.user import UserRegistrationAPIView


api_urls = [
    path('rooms/', include('rooms.urls.room')),
    path('messages/', include('chat_messages.urls.messages')),
    path('user/register/', UserRegistrationAPIView.as_view(), name='user-register'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
