from rest_framework import status
from rest_framework.response import Response
from iasip_api.models import Character
from iasip_api.serializers import CharacterSerializer
from django.http import Http404
from rest_framework.views import APIView


class CharacterList(APIView):
    """
    List all characters, or create a new one
    """
    def get(self, request, format=None):
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterDetail(APIView):
    """
    Retrieve, update, or delete a character instance.
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

    def put(self, request, pk, format=None):
        character = self.get_object(pk)
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        character = self.get_object(pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


