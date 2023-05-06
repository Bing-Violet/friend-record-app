from rest_framework import serializers
from .models import Character
from event.serializers import EventCreateSerializer

class CharacterSerializer(serializers.ModelSerializer):
	event = EventCreateSerializer(many=True)
	
	class Meta:
		model = Character
		fields = [
			"id",
			"name",
			"user",
			"sum",
			"thumbnail",
			"last_log",
			"created_on",
			"event"

		]

class CharacterCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Character
		fields = [
			"id",
			"name",
			"user",
			"sum",
			"thumbnail",
			"last_log",
			"created_on",

		]