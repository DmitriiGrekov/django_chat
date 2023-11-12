from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers.users import UserRegistrationSerializer
from core.serializers.users import UserSerializer


class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)