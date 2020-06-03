#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),  # 文章列表
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),  # 文章详情
    path('article-create/', views.article_create, name='article_create'),  # 文章创建
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),  # 文章删除
    path('article-update/<int:id>/', views.article_update, name='article_update'),  # 文章更新
    path('article-own/', views.article_own, name='article_own'),  # 查看自己的文章列表
    path('article-search/', views.article_search, name='article_search'),  # 文章名搜索
    path('article-own-search/', views.article_own_search, name='article_own_search'),  # 自己的文章名搜索
    path('', views.up_likes_num, name="up_likes_num"),  # 点赞操作
]
