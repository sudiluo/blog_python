from django.contrib import admin
from .models import models

admin.site.register(models.article)
admin.site.register(models.OrderModel)