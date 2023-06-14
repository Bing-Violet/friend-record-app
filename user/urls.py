from django.urls import path, include
from .apis import UserCreateApi, UserListApi, UserDetailApi, UserLoginApi, EmailVerify, SendPasswordChange, PasswordChange

urlpatterns = [
  path('user-create/', UserCreateApi.as_view()),
  path('user-login/', UserLoginApi.as_view()),
  path('user-list/', UserListApi.as_view()),
  path('user-detail/<UID>', UserDetailApi.as_view()),
  path('email-verify/', EmailVerify.as_view()),
  path('send-password-change/', SendPasswordChange.as_view()),
  path('password-change/', PasswordChange.as_view()),
  # path("", index, name="index"),
  ]