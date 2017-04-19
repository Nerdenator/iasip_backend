from rest_framework import serializers

from iasip_api.models import Character, Crimes, CharacterCrime


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='character-highlight', format='html')

    class Meta:
        model = Character
        fields = ('url', 'id', 'first_name', 'last_name', 'preferred_name', 'owner', 'highlight',)


class CrimeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Crimes
        fields = ('url', 'id', 'criminal_charge', 'degree', 'charge_type', 'charge_class', 'jurisdiction', 'owner')


class CharacterCrimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterCrime
        fields = ('url', 'crime', 'season', 'episode')
