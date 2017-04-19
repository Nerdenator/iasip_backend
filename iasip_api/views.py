from iasip_api.models import CharacterCrime, Character, Crimes
from iasip_api.serializers import CharacterSerializer, CharacterCrimeSerializer
from rest_framework import mixins, generics


class CharacterList(mixins.ListModelMixin, generics.GenericAPIView):
    """
    List all characters.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CharacterDetail(mixins.RetrieveModelMixin,
                      generics.GenericAPIView):
    """
    Show detail for a specific character
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

