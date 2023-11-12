from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from chat_messages.models.message import MessageModel
from chat_messages.serializers.messages import MessageSerializer
from chat_messages.serializers.messages import MessageCreateSerializer


class MessagesListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, room_id):
        qs = MessageModel.objects.filter(room__sid=room_id)
        serializer = MessageSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, room_id):
        data = request.data
        data['user_id'] = request.user.id
        data['room_id'] = room_id
        serializer = MessageCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        return Response(message)

        

        