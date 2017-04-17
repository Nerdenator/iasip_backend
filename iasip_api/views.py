from iasip_api.models import Character
from iasip_api.permissions import IsOwnerOrReadOnly
from iasip_api.serializers import CharacterSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User

class CharacterList(generics.ListCreateAPIView):
    """
    List all characters, or create a new one
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

