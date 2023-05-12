from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EventCreateSerializer
from .models import Event
from character.models import Character

class OwnerOnlyRestriction(UserPassesTestMixin):
    '''
    restriction of owner user can access the user data
    '''
    def test_func(self):
        print('in_testfun')
        owner_user = self.request.user
        object_user = self.get_object()
        print("owner",owner_user, "object",object_user)
        verification = True if owner_user.is_staff or owner_user==object_user else False
        return verification
    
    def handle_no_permission(self):
        return JsonResponse({"info":"not allowed"},status=403)

class EventCreateApi(generics.CreateAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


class EventListApi(generics.ListAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


class EventUserListApi(APIView):
    # get characterevent list.
    def post(self, request):
        character_uid = request.data.pop('character')
        character_event = Event.objects.filter(character=character_uid)
        serializer = EventCreateSerializer(character_event, many=True)
        return Response(serializer.data)


class EventDetailApi(OwnerOnlyRestriction, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'

    def perform_update(self, serializer):
        pre_instance = self.get_object()  # instance before update
        instance = serializer.save()
        diff_money = instance.money - pre_instance.money
        character = Character.objects.get(id=instance.character.id)
        character.sum += diff_money
        character.save()

    def perform_destroy(self, instance):
        character = Character.objects.get(id=instance.character.id)
        character.sum -= instance.money
        instance.delete()
        character.save()  