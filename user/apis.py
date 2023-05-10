from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.http import Http404
from django.db import IntegrityError


from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response



from .serializers import UserCreateSerializer
from .models import User


from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }


class UserCreateApi(APIView):
    def post(self, request, format=None):
        try:
            user = User.objects.create(** request.data)
            tokens = get_tokens_for_user(user)
            serializer = UserCreateSerializer(user)
            return JsonResponse({"user":serializer.data, "tokens":tokens}, status=200)
        except IntegrityError as e:
            # assumption is that email requested is already registered
            return JsonResponse({'message':'this email is already in use.'}, status=400)
        except:
            raise Http404

class UserLoginApi(APIView):
    def post(self, request, format=None):
        try:
            user = User.objects.get(** request.data)
            tokens = get_tokens_for_user(user)
            serializer = UserCreateSerializer(user)
            return JsonResponse({"user":serializer.data, "tokens":tokens}, status=200)
        except User.DoesNotExist as e:
            raise Http404


class UserListApi(generics.ListAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    lookup_field = 'UID'


