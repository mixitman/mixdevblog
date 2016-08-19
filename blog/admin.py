from django.contrib import admin

# Register your models here.
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "created_date", "published_date"]

admin.site.register(Post, BlogAdmin)
