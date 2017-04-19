from rest_framework import serializers
from iasip_api.models import Character, Crime, CharacterCrime


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'created', 'first_name', 'last_name', 'preferred_name', 'crimes')


class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime
        fields = ('id', 'created', 'criminal_charge', 'degree', 'charge_type', 'jurisdiction')


class CharacterCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterCrime
        fields = ('id', 'character', 'crime', 'season', 'episode')
