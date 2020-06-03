from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class PhotoPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author是user的外键
    name = models.CharField(max_length=50)  # 图片名称
    # upload_to 指定上传文件位置
    # 这里指定存放在 image/ 目录下
    path = models.FileField(upload_to="image/")  # 上传路径
    created_at = models.DateTimeField(default=timezone.now)  # 上传时间

    class Meta:
        # 元数据选项
        ordering = ('-created_at',)  # 设置顺序

    # 返回名称
    def __str__(self):
        return self.name

