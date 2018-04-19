from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^index/', views.index, name='index'),
    url(r'^loginUser/', views.loginUser, name='loginUser'),
    url(r'^loginIndex/', views.loginIndex, name='loginIndex'),
]
