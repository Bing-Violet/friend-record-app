from django.contrib import admin
from .models import Character

# class CharacterAdmin(admin.ModelAdmin):
#     readonly_fields = ('last_log',)

admin.site.register(Character)