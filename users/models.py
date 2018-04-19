from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    user_type = models.CharField(max_length=20,default=0,blank=False)
    images_url = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=18,blank=False,default='')
    class Meta(AbstractUser.Meta):
        ordering = ['id']
        pass