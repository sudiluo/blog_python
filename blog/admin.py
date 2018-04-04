from django.contrib import admin
from .models import Post, Category, Tag

#Django后台管理类
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

#注册类到后台去管理
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)