from iasip_api.models import Character
from iasip_api.serializers import CharacterSerializer
from rest_framework import generics

class CharacterList(generics.ListCreateAPIView):
    """
    List all characters, or create a new one
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

