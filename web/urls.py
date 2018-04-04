from . import views
from . import views_data
from django.urls import path

# url路由配置
urlpatterns = [
    # path Django2.0语法 兼容2.0以下版本 参数1：访问路径，参数2：视图函数
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('data/', views_data.data, name='data'),
    path('add/', views.add ),
]
