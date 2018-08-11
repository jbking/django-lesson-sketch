from django.shortcuts import render

from .models import Post


def post_list(request):
    post_list = Post.objects.filter(published_date__isnull=False)
    return render(request, 'blog/post_list.html', {'post_list': post_list})


def post_detail(request, pk):
    context_object_name = 'post'
    post = Post.objects.filter(published_date__isnull=False).get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
