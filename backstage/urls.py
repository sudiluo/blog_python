from django.conf.urls.static import static
from django.template.defaulttags import url

from blog.urls import app_name
from ulife import settings
from . import views
from django.urls import path

app_name = 'backstage'

# url路由配置
urlpatterns = [
    # path Django2.0语法 兼容2.0以下版本 参数1：访问路径，参数2：视图函数
    path('index/', views.index, name='index'),
    path('login/', views.loginUser, name='loginUser'),
    path('userList/', views.UserListView.as_view(), name='userList'),
    path('findUser/', views.findUser, name='findUser'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('productList/', views.ProductListView.as_view(), name='productList'),
    path('categoryList/', views.CategoryListView.as_view(), name='categoryList'),
    path('productOrderList/', views.ProductOrderListView.as_view(), name='productOrderList'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'),
    path('static/', views.upload_avatar, name='upload_avatar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = views.page_not_found
