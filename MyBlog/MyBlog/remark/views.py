from django.shortcuts import redirect
# Create your views here.
from .models import Remark

from article.models import ArticlePost


def remark(request,id):
    if request.method == 'POST':
        n_remark = Remark()
        remarker = request.user
        content = request.POST.get('text','')
        n_remark.remarker = remarker
        n_remark.content = content
        n_remark.article_id = id

        n_remark.save()
        article = ArticlePost.objects.get(id=id)
        article.remarks_num += 1
        article.save()

        return redirect("article:article_detail", id=id)