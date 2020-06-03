from django.db import models

# Create your models here.
from article.models import ArticlePost


class Remark(models.Model):
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name="remark")  # 所属文章
    remarker = models.CharField(max_length=90)  # 评论者
    content = models.TextField()  # 评论内容
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        ordering = ('-created_at',)  # 按照时间从晚到早排列

    def __str__(self):
        return "Comment by {0} on {1}".format(self.remarker, self.article)

