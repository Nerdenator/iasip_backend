from iasip_api.models import CharacterCrime, Character, Crimes
from iasip_api.serializers import CharacterSerializer, UserSerializer, CharacterCrimeSerializer
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class CharacterList(APIView):
    """
    List all characters.
    """
    def get(self, request, format=None):
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)


class CharacterCrimeList(APIView):
    """
    Show all CharacterCrimes.
    """
    def get(self, request, format=None):
        characterCrimes = CharacterCrime.objects.all()
        serializer = CharacterSerializer


