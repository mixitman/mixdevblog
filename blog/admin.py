from django.contrib import admin
from django import forms
from django.db import models
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_date", "published_date", "author"]
    list_filter = ["created_date", "published_date", "author"]
    search_fields = ["title", "article"]
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Meta:
        model = Post

    class Media:
        js = ('ckeditor/ckeditor.js',)

admin.site.register(Post, BlogAdmin)
