from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .serializers import CharacterCreateSerializer, CharacterSerializer
from .models import Character

class CharacterCreateApi(generics.CreateAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class CharacterListApi(generics.ListAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class UserCharacterListApi(APIView):
    def post(self, request):
        user_uid = request.data.pop('user')
        character_list = Character.objects.filter(user=user_uid)
        serializer = CharacterSerializer(character_list, many=True)
        return Response(serializer.data)
        
class CharacterDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    lookup_field = 'id'