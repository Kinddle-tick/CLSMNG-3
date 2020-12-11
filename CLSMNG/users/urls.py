"""为app users定义url模式"""
from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views

app_name='users'
urlpatterns = [
    #登陆页面
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.register, name = 'register'),
]