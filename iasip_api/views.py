from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from iasip_api.models import Character
from iasip_api.serializers import CharacterSerializer


@api_view(['GET', 'POST'])
def character_list(request, format=None):
    """
    List all characters, or create a new one.
    """
    if request.method == 'GET':
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CharacterSerializer(data=request.data)
        if serialier.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def character_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a character.
    """
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

