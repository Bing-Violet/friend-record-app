from django.urls import path, include
from .apis import EventCreateApi, EventListApi, EventDetailApi

urlpatterns = [
  path('event-create/', EventCreateApi.as_view()),
  path('event-list/', EventListApi.as_view()),
  path('event-detail/<id>', EventDetailApi.as_view()),
  ]