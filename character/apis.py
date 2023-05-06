from django.shortcuts import render

from rest_framework import generics

from .serializers import CharacterCreateSerializer, CharacterSerializer
from .models import Character

class CharacterCreateApi(generics.CreateAPIView):
    serializer_class = CharacterCreateSerializer
    queryset = Character.objects.all()


class CharacterListApi(generics.ListAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()

class CharacterDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    lookup_field = 'id'