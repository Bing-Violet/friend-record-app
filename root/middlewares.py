from django.http import HttpResponse
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
import os
from user.models import User
from rest_framework import authentication
import jwt
from django.contrib.auth.middleware import get_user
from django.utils.functional import SimpleLazyObject


class JWTAuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda:self.__class__.get_jwt_user(request))
        print('ch',request)
        return self.get_response(request)

    @staticmethod
    def get_jwt_user(request):
        print('IN STATIC')

        # if user.is_authenticated:
        #     return user
        # jwt_authentication = JSONWebTokenAuthentication()
        # if jwt_authentication.get_jwt_value(request):
        #     user, jwt = jwt_authentication.authenticate(request)
        # return user

class HttpResponseBadRequest(JsonResponse):
    status_code = 400




from user.models import User
from rest_framework import authentication

class JWTAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        
        print("HEARDER",request.headers)
        print("USER",request.user)
        # print("AUTH",request.auth)

        return self.get_response(request)