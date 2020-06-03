#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='login'),  # 登录
    path('logout/', views.user_logout, name='logout'),  # 登出
    path('register/', views.user_register, name='register'),  # 注册
    path('info/', views.user_info, name='info'),  # 查看用户信息
    path('edit/', views.user_edit, name='edit'),  # 编辑用户信息
    path('delete/<int:id>/', views.user_delete, name='delete'),  # 删除用户
]
