from rest_framework import serializers

from iasip_api.models import Character, Crimes, CharacterCrime


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('url', 'id', 'first_name', 'last_name', 'preferred_name',)


class CrimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crimes
        fields = ('url', 'id', 'criminal_charge', 'degree', 'charge_type', 'charge_class', 'jurisdiction')


class CharacterCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterCrime
        fields = ('url', 'crime', 'season', 'episode')
