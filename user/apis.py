from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.http import Http404
from django.db import IntegrityError


from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



from .serializers import UserCreateSerializer, UserSerializer
from .models import User
from .email_validation.senders import SendVerificationEmail, SendPasswordReset

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }

class UserCreateApi(APIView):

    def post(slef, request, format=None):
        user = User.objects.create_user(**request.data)
        # user.email_verified = False
        user.save()

        token = str(Token.objects.create(user=user))
        print("token", type(token))
        request_data = {
            "email":user.email,
            "verification_token":token
        }
        sender = SendVerificationEmail(request_data)
        result = sender.send()
        result["UID"] = user.UID
        return  JsonResponse(result)


class EmailVerify(APIView):
    # authentication_classes = ([J])
    # permission_classes = ([IsAuthenticated])
    def post(self, request, format=None):
       
        token = request.data.get("token")
        try:
            user = User.objects.get(auth_token=token)
            if not user:
                return JsonResponse({"verification":False}, status=404)
            user.email_verified = True
            auth_token = Token.objects.get(user=user)
            auth_token.delete()
            user.save()
            token = get_tokens_for_user(user)
            serializer = UserSerializer(user)
            return JsonResponse({"verification":True,"user":serializer.data, "tokens":token}, status=200)
        except Exception as e:
            return JsonResponse({"verification":False}, status=404)


class UserLoginApi(APIView):
    def post(self, request, format=None):
        try:
            email = request.data.get('email')
            userExist = User.objects.filter(email=email).exists()
            user = User.objects.get(** request.data)
            tokens = get_tokens_for_user(user)
            serializer = UserCreateSerializer(user)
            return JsonResponse({"user":serializer.data, "tokens":tokens}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'user_exist':True if userExist else False}, status=404)


class PasswordChange(APIView):
    def post(self, request, format=None):
        password = request.data.get("password")
        token = request.data.get("token")
        print("password-change", password, token)
        try:
            user = User.objects.get(auth_token=token)
            print(user)
            if not user:
                return JsonResponse({"password_change":False}, status=404)
            user.set_password(password)
            user.save()
            auth_token = Token.objects.get(user=user)
            auth_token.delete()
            token = get_tokens_for_user(user)
            serializer = UserCreateSerializer(user)
            return JsonResponse({"password_change":True, "tokens":token,"user":serializer.data}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"password_change":False}, status=404)


class SendPasswordChange(APIView):

    def post(slef, request, format=None):
        print("PASSRE",request.data.get("email"))
        email = request.data.get("email")
        user = User.objects.get(email=email)
        if not user:
            return JsonResponse("no user")
        try:
            token = Token.objects.get(user=user)
            print("TOKEN_EXIST???",token)
            token.delete()
        except Exception as e:
            print("token doesn't exist", e)
        finally:
            token = str(Token.objects.create(user=user))
            print("token", token)
            request = {
                "email":user.email,
                "verification_token":token,
                "title":"[neko-japanese]password-change"

            }
            sender = SendPasswordReset(request)
            result = sender.send()
            print("result", result)
            return  JsonResponse(result)

class UserListApi(generics.ListAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    lookup_field = 'UID'


