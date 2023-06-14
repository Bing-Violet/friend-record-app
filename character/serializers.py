from rest_framework import serializers
from .models import Character
from event.serializers import EventCreateSerializer
from event.models import Event

class CharacterSerializer(serializers.ModelSerializer):
	event = EventCreateSerializer(many=True, required=False, allow_null=True)
	event_length = serializers.SerializerMethodField('get_eventLengthe')
	class Meta:
		model = Character
		fields = [
			"id",
			"name",
			"user",
			"sum",
			"birthday",
			"thumbnail",
			"avatar",
			"last_log",
			"created_on",
			"event",
			"event_length",
		]
	def get_eventLengthe(self, instance):
		count = Event.objects.filter(character=instance.id)
		return len(count)

class CharacterCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Character
		fields = [
			"id",
			"name",
			"user",
			"sum",
			"thumbnail",
			"avatar",
			"last_log",
			"created_on",

		]