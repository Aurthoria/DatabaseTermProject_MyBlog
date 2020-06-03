from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Notice(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author是user的外键
    content = models.TextField(null=False)  # 公告内容
    created_at = models.DateTimeField(default=timezone.now)  # 创建时间

    class Meta:
        ordering = ['-created_at']
        db_table = "notice"

