from django.db import models

from user.models import User

from datetime import timezone
import datetime


class Character(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, default=None, related_name='character', on_delete=models.CASCADE)
    last_log = models.DateTimeField(auto_now_add=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ['-last_log',]