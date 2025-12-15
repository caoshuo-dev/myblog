from django.shortcuts import render
from .models import Post  # 从当前目录的models.py中导入Post模型


def post_list(request):
    """
    处理博客文章列表的视图函数。
    1. 从数据库中获取所有文章，按创建时间倒序排列（新的在前）。
    2. 将文章列表传递给名为 'blog/list.html' 的模板进行渲染。
    """
    posts = Post.objects.all().order_by('-created_time')  # 获取所有文章，按创建时间倒序排序
    return render(request, 'blog/list.html', {'posts': posts})  # 渲染模板，并传入文章数据


def post_detail(request, pk):  # pk 是接收来自URL的文章ID
    # 获取特定ID的文章，如果不存在则返回404页面
    post = Post.objects.get(id=pk)
    return render(request, 'blog/detail.html', {'post': post})


def about(request):
    """‘关于我’页面视图"""
    return render(request, 'blog/about.html')
