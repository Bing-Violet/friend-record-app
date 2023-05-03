from django.shortcuts import render

from rest_framework import generics

from .serializers import EventCreateSerializer
from .models import Event

class EventCreateApi(generics.CreateAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


class EventListApi(generics.ListAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()

class EventDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'