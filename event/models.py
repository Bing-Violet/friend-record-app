from django.db import models

from character.models import Character

from datetime import timezone
import datetime


class Event(models.Model):
    name = models.CharField(max_length=30)
    character = models.OneToOneField(Character, default=None, related_name='event', on_delete=models.CASCADE)
    money = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ['-money',]