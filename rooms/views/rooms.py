from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from rooms.models.room import RoomModel
from rooms.serializers.room import RoomSerializer


class RoomModelViewSet(ModelViewSet):
    """Вьюшка комнат."""

    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = self.queryset
        return qs.filter(users=self.request.user)