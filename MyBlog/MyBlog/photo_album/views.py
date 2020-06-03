from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import PhotoPost
from .forms import PhotoPostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def photo_add(request):
    # 判断是否为 post 方法提交
    if request.method == "POST":
        af = PhotoPostForm(request.POST, request.FILES)
        # 判断表单值是否合法
        if af.is_valid():
            name = af.cleaned_data['name']
            path = af.cleaned_data['path']
            img = PhotoPost(name=name, path=path)
            user_id = request.user.id
            img.author = User.objects.get(id=user_id)
            img.save()
            return redirect("photo_album:photo_own")
    else:
        af = PhotoPostForm()
        return render(request, 'photo_album/add.html', context={"af": af})


def photo_own(request):
    photos = PhotoPost.objects.filter(author_id=request.user.id)  # 返回一个迭代器，可以返回多个数据

    context = {'photos': photos}
    return render(request, 'photo_album/own.html', context)


@login_required(login_url='/account/login/')
def photo_detail(request, id):
    img = PhotoPost.objects.get(id=id)

    return render(request, 'photo_album/detail.html', context={"img": img})


@login_required(login_url='/account/login/')
def photo_delete(request, id):
    photo = PhotoPost.objects.get(id=id)
    photo.delete()
    return redirect("photo_album:photo_own")


def photo_search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return HttpResponse(error_msg)

    photos = PhotoPost.objects.filter(name__icontains=q,author_id=request.user.id)
    context = {'photos': photos}
    return render(request, 'photo_album/own.html', context)


