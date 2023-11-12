from rest_framework.routers import DefaultRouter

from rooms.views.rooms import RoomModelViewSet

router = DefaultRouter()
router.register(r'', RoomModelViewSet, basename='room')

urlpatterns = router.urls