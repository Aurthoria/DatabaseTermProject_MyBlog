from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone


class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)  # author是user的外键
    title = models.CharField(max_length=100)  # 标题
    content = models.TextField()  # 内容
    created_at = models.DateTimeField(default=timezone.now)  # 创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间
    likes_num = models.IntegerField(default=0)  # 点赞数
    remarks_num = models.IntegerField(default=0) # 评论数

    class Meta:
        # 元数据选项
        ordering = ('-created_at',)  # 设置顺序

    def __str__(self):
        return self.title  # 返回标题
