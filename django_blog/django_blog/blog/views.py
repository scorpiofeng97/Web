from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNoExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)

    else:
        post_list = Post.get_all_normal()
        if category_id:
            post_list = post_list.filter(category_id=category_id)

    return render(request, 'blog/list.html', context={'post_list': post_list})


def post_detail(request, post_id):

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNoExist:
        post = None
    return render(request, 'blog/detail.html', context={'post': post})
