from django.urls import path, include
from .apis import CharacterCreateApi, CharacterListApi, CharacterDetailApi

urlpatterns = [
  path('character-create/', CharacterCreateApi.as_view()),
  path('character-list/', CharacterListApi.as_view()),
  path('character-detail/<id>', CharacterDetailApi.as_view()),
  ]