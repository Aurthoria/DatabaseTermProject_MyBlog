"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),  # 后台管理模块
                  path('account/', include('account.urls', namespace='account')),  # 用户模块
                  path('', views.user_login),  # 默认界面为用户登陆模块
                  path('article/', include('article.urls', namespace='article')),  # 文章模块
                  path('remark/', include('remark.urls', namespace='remark')),  # 评论模块
                  path('photo_album/', include('photo_album.urls', namespace='photo_album')),  # 相册模块
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 添加图片的静态路径
