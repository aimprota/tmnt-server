from rest_framework import serializers

from tmnt.models import Character

class CharacterSerializer(serializers.ModelSerializer):
	class Meta:
		model = CharacterSerializer
		fields = ('id', 'name', 'team', 'created')
