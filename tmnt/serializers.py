from rest_framework import serializers

from tmnt.models import Character, Team

class CharacterSerializer(serializers.ModelSerializer):

  class Meta:
    model = Character
    fields = ('id', 'name')

class TeamSerializer(serializers.ModelSerializer):

  characters = CharacterSerializer(many=True)

  class Meta:
    model = Team
    fields = ('id', 'name', 'characters')
