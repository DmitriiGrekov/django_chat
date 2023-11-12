from rest_framework import serializers

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from chat_messages.models.message import MessageModel

from core.serializers.users import UserSerializer
from core.exceptions import CustomAPIException

from rooms.serializers.room import RoomSerializer
from rooms.models.room import RoomModel


class MessageSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    
    class Meta:
        model = MessageModel
        fields = ['sid', 'text', 'created_at', 'updated_at', 'room', 'user']


class MessageCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания сообщения."""
    user_id = serializers.IntegerField()
    room_id = serializers.UUIDField()
    text = serializers.CharField()

    class Meta:
        model = MessageModel
        fields = ['user_id', 'room_id', 'text']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        room = RoomModel.objects.filter(pk=validated_data.get('room_id'), users__id=validated_data.get('user_id')).first()
        if not room:
            raise CustomAPIException('Вы не состоите в этой комнате')
        message = MessageModel.objects.create(**validated_data)
        serializer = MessageSerializer(message).data

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{room.sid}',
            {
                'type': 'chat.message',
                'message': serializer,  # ваше сообщение
                })
        return serializer