from rest_framework import serializers

from core.serializers.users import UserSerializer

from rooms.models.room import RoomModel


class RoomSerializer(serializers.ModelSerializer):
    """Сериализатор модели комнаты."""
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = RoomModel
        fields = ['sid', 'name', 'users']