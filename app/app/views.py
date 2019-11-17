from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView

from rest_framework.response import Response

from .models import Detail
from .serializers import DetailSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class DetailList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    name = 'detail-list'


class DetailDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    name = 'detail-detail'


class UserCreate(APIView):
    serializer_class = UserSerializer
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    name = 'user-list'


class ValidateJWT(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data, status=status.HTTP_200_OK)

