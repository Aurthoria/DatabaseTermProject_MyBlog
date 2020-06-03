#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import ArticlePost
from django.db import models


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'content')
