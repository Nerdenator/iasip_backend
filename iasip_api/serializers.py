from rest_framework import serializers

from iasip_api.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character 
        fields = ('first_name', 'last_name', 'preferred_name')

