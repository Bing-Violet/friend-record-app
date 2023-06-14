from django.urls import path, include
from .apis import CharacterCreateApi, CharacterListApi, CharacterDetailApi, UserCharacterListApi, CharacterBirthdayUpdateApi

urlpatterns = [
  path('character-create/', CharacterCreateApi.as_view()),
  path('character-list/', CharacterListApi.as_view()),
  path('user-character/', UserCharacterListApi.as_view()),
  path('character-detail/<id>', CharacterDetailApi.as_view()),
   path('birthday-update/', CharacterBirthdayUpdateApi.as_view()),
  ]