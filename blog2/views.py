from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post


class PostListView(ListView):

    model = Post
    context_object_list = 'post_list'
    queryset = Post.objects.filter(published_date__isnull=False)


class PostDetailView(DetailView):

    model = Post
    context_object_name = 'post'
    queryset = Post.objects.filter(published_date__isnull=False)
