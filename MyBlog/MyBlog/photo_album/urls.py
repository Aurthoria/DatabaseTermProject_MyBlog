#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'photo_album'

urlpatterns = [
    path('photo_add/', views.photo_add, name='photo_add'),  # 上传图片
    path('photo_own/', views.photo_own, name='photo_own'),  # 图片列表
    path('photo_detail/<int:id>/', views.photo_detail, name='photo_detail'),  # 查看大图
    path('photo_delete/<int:id>/', views.photo_delete, name='photo_delete'),  # 删除图片
    path('photo_search/', views.photo_search, name='photo_search'),  # 图片名搜索
]
