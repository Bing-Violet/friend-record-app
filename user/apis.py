from django.shortcuts import render

from rest_framework import generics

from .serializers import UserCreateSerializer
from .models import User

class UserCreateApi(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserListApi(generics.ListAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    lookup_field = 'UID'