from django.db import models

from user.models import User

from datetime import timezone
import datetime


class Character(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='character', default=None, on_delete=models.CASCADE)
    sum = models.IntegerField(default=0)
    thumbnail = models.ImageField(blank=True, null=True, default='default.png')
    last_log = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)


    class Meta:
        ordering = ['-last_log',]

    def __str__(self):
        return self.name