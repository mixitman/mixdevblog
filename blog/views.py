from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from .models import Post


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, './blog/create.html', context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, './blog/detail.html', context)


def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts_list, 3)  # Show xx contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    context = {
        'title': "The Blog",
        'posts': posts,
        "page_request_var": page_request_var,
    }
    return render(request, './blog/blog.html', context)


def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,  request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, './blog/create.html', context)


def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()

    return redirect("blog:post_list")




