# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import markdown  # 使用markdonw渲染

from remark.models import Remark


def article_list(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        articles = ArticlePost.objects.all()
        context = {'articles': articles}
        return render(request, 'article/list.html', context)
    else:
        articles = ArticlePost.objects.all()
        context = {'articles': articles}
        return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])

    remark = Remark.objects.all()
    context = {
        'article': article,
        'remark': remark.filter(article_id=id),
    }
    return render(request, 'article/detail.html', context)


@login_required(login_url='/account/login/')
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            user_id = request.user.id
            new_article.author = User.objects.get(id=user_id)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)


@login_required(login_url='/account/login/')
def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")


@login_required(login_url='/account/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.content = request.POST['content']
            article.save()

            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写")

    else:
        article_post_form = ArticlePostForm()
        context = {'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/update.html', context)


def article_own(request):
    articles = ArticlePost.objects.filter(author_id=request.user.id)  # 返回一个迭代器，可以返回多个数据

    context = {'articles': articles}
    return render(request, 'article/own.html', context)


def article_search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return HttpResponse(error_msg)

    articles = ArticlePost.objects.filter(title__icontains=q)
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


def article_own_search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return HttpResponse(error_msg)

    articles = ArticlePost.objects.filter(title__icontains=q, author_id=request.user.id)
    context = {'articles': articles}
    return render(request, 'article/own.html', context)


@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def up_likes_num(request):
    article_id = request.POST.get("id")
    action = request.POST.get("action")
    if article_id and action:
        article = ArticlePost.objects.get(id=article_id)
        article.likes_num += 1
        article.save()
        return HttpResponse('success')
    else:
        return HttpResponse('-1')
