from django.db import models


from uuid import uuid4
from datetime import timezone
import datetime


class Character(models.Model):
    name = models.CharField(max_length=30)
    last_log = models.DateTimeField(auto_now_add=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ['-last_log',]