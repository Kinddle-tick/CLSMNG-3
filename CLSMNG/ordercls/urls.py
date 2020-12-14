#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Kinddle

from . import views
from django.urls import path

app_name='ordercls'
urlpatterns =[
    path('', views.default),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('feedback/', views.feedback, name='feedback'),
    path('order/', views.order, name='order'),
    path('my_request/', views.my_request,name='my_request')
]