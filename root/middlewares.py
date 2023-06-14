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
from django.utils.deprecation import MiddlewareMixin

class CustomHeaderMiddleware(MiddlewareMixin):
    def process_request(self, request, data):
        request.META['AUTH_USER'] = data
class HttpResponseBadRequest(JsonResponse):
    status_code = 400




from user.models import User
from rest_framework import authentication

class JWTAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        '''
        Recieve request from middleware. If the request header includes JWT, request.user will be authenticated user  
        '''
        print("IN _CALL")
        auth_data = authentication.get_authorization_header(request)
        print("IN _CALL", auth_data)
        if not auth_data:
            return self.get_response(request) 
        prefix,decode = auth_data.decode('utf-8').split(' ')
        try:
            # if JWT is invalid or expired, return error
            payload = jwt.decode(decode, settings.JWF_SECRET_KEY, algorithms="HS256")
            request.user = User.objects.get(UID=payload['user_id'])
            print("USER",request.user.last_login)
            return self.get_response(request)
        except jwt.DecodeError as identifier:
            # return HttpResponse(identifier, status=500)
            return HttpResponseBadRequest({"message":'Your token is invalid', "token_not_pass":True})
            # raise exceptions.AuthenticationFailed(
            #     'Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            return HttpResponseBadRequest({"message":'Your token is expired', "token_not_pass":True})
            # raise exceptions.AuthenticationFailed(
        #     'Your token is expired,login')