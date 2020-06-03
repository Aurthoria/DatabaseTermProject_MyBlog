from django import forms
from .models import PhotoPost


# 表单类用以生成表单
class PhotoPostForm(forms.Form):
    name = forms.CharField()
    path = forms.FileField()
