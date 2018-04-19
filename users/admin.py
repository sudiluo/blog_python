from django.contrib import admin

from backstage.models import MallProduct, MallProductCategory, MallProductOrder
from .models import User

admin.site.register(User)
admin.site.register(MallProduct)
admin.site.register(MallProductCategory)
admin.site.register(MallProductOrder)
