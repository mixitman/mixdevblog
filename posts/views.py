from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post


def post_create(request):
    context = {
        "title": "Create"
    }
    return render(request, "blog_list.html", context)


def post_detail(request):
    instance = get_object_or_404(Post, id=3)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "blog_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "object_list": queryset
    }
    return render(request, "blog_list.html", context)


def post_update(request):
    context = {
        "title": "Update"
    }
    return render(request, "blog_list.html", context)


def post_delete(request):
    context = {
        "title": "Delete"
    }
    return render(request, "blog_list.html", context)
