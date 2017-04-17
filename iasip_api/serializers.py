from django.contrib.auth.models import User
from rest_framework import serializers

from iasip_api.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    owner = serializer.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='character-highlight', format='html')

    class Meta:
        model = Character
        fields = ('url', 'first_name', 'last_name', 'preferred_name')


class UserSerializer(serializers.ModelSerializer):
    characters = serializers.HyperlinkedRelatedField(many=True, view_name='character-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'characters', 'owner',)

