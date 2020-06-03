from django.contrib import admin
from article.models import ArticlePost
from photo_album.models import PhotoPost
from remark.models import Remark
from notice.models import Notice


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("author", 'title', 'created_at', 'updated_at', 'content')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("author", 'name', 'created_at', 'path')


class RemarkAdmin(admin.ModelAdmin):
    list_display = ("article", 'remarker', 'created_at', 'content')


class NoticeAdmin(admin.ModelAdmin):
    list_display = ("author", 'content', 'created_at')


admin.site.register(ArticlePost, ArticleAdmin)
admin.site.register(PhotoPost, PhotoAdmin)
admin.site.register(Remark, RemarkAdmin)
admin.site.register(Notice, NoticeAdmin)
