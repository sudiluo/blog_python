from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    usertype = models.CharField(max_length=20,default=0)
    imagesurl = models.CharField(max_length=20, blank=True)
    class Meta(AbstractUser.Meta):
        ordering = ['id']
        pass