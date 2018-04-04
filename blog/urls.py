from django.conf.urls import url
from blog.feeds import AllPostsRssFeed
from . import views
from django.urls import include
# 视图函数命名空间
app_name = 'blog'

# url路由配置
urlpatterns = [
    # path Django2.0语法 兼容2.0以下版本 参数1：访问路径，参数2：视图函数
    # path('', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    url(r'^search/', include('haystack.urls')),
]
