#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'remark'

urlpatterns = [
    path('<int:id>/', views.remark, name='remark'),  # 进行评论操作，id是文章id
]
