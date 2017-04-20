from django.http import Http404

from iasip_api.models import CharacterCrime, Character, Crime
from iasip_api.serializers import CharacterSerializer, CrimeSerializer, CharacterCrimeSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetail(APIView):
    """
    Retrieve a character instance
    """
    def get_object(self, pk):
        try:
            return Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        character = self.get_object(pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)


class CrimeList(generics.ListAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer


class CrimeDetail(APIView):
    """
    Retrieve a crime definition
    """
    def get_object(self, pk):
        try:
            return Crime.objects.get(pk=pk)
        except Crime.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        crime = self.get_object(pk=pk)
        serializer = CrimeSerializer(crime)
        return Response(serializer.data)


class CharacterCrimeList(generics.ListAPIView):
    queryset = CharacterCrime.objects.all()
    serializer_class = CharacterCrimeSerializer


class CharacterCrimeDetail(APIView):
    """
    Retrieve a character, then their crimes
    """
    def get_object(self, pk):
        try:
            return CharacterCrime.objects.get(character__id=pk)
        except CharacterCrime.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        character_crimes = self.get_object(pk=pk)
        serializer = CharacterCrimeSerializer(character_crimes)
        return Response(serializer.data)