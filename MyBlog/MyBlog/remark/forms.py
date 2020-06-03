from django import forms
from MyBlog.remark.models import Remark


class RemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ("remark", "content",)