from django.urls import path, include
from .apis import UserCreateApi, UserListApi, UserDetailApi

urlpatterns = [
  path('user-create/', UserCreateApi.as_view()),
  path('user-list/', UserListApi.as_view()),
  path('user-detail/<UID>', UserDetailApi.as_view()),
  ]