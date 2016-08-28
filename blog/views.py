from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from .models import Post


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, './blog/create.html', context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.published_date > timezone.now() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, './blog/detail.html', context)


def post_list(request):
    queryset_list = Post.objects.filter(draft=False)\
        .filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all().order_by('-published_date')

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(article__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 3)  # Show xx contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'title': "Loving Open Source",
        'posts': queryset,
        "page_request_var": page_request_var,
    }
    return render(request, './blog/blog.html', context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()

    return redirect("blog:post_list")




