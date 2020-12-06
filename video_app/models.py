

# Create your models here.

from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)

    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=150)


    def __str__(self):
        return self.user.username    