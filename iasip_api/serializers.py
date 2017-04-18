from django.contrib.auth.models import User
from rest_framework import serializers

from iasip_api.models import Character, Crime


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='character-highlight', format='html')

    class Meta:
        model = Character
        fields = ('url', 'id', 'first_name', 'last_name', 'preferred_name', 'owner', 'highlight',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    characters = serializers.HyperlinkedRelatedField(many=True, view_name='character-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'characters', )


class CrimeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Crime
        fields = ('url', 'id', 'criminal_charge', 'degree', 'charge_type', 'charge_class', 'jurisdiction', 'owner')
