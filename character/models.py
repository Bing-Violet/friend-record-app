from django.db import models

from user.models import User

from django.utils import timezone



class Character(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='character', default=None, on_delete=models.CASCADE)
    sum = models.IntegerField(default=0)
    thumbnail = models.ImageField(blank=True, null=True, default='default.png')
    avatar = models.CharField(max_length=50, default=None, null=True, blank=True)
    last_log = models.DateTimeField(auto_now_add=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)


    class Meta:
        ordering = ['-last_log',]

    def __str__(self):
        return self.name