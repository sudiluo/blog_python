from blog.urls import app_name
from . import views
from django.urls import path

app_name = 'backstage'

# url路由配置
urlpatterns = [
    # path Django2.0语法 兼容2.0以下版本 参数1：访问路径，参数2：视图函数
    path('index/', views.index, name='index'),
    path('login/', views.loginUser, name='loginUser'),
    path('userList/', views.userList, name='userList'),
]
