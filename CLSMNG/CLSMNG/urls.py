"""CLSMNG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render,redirect

urlpatterns = [
    path('', lambda request: render(request, 'index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('ordercls/', include('ordercls.urls')),
    path('timetable/', include('timetable.urls')),
    # path('monitor/', include('monitor.urls')),
    path('users/', include('users.urls')),
    path('<htmls>', lambda request, htmls: render(request, htmls))# 便于初期调试查看html, 之后建议删除
]
