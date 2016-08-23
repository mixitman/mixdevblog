from django.contrib import admin

from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_date", "published_date", "author"]
    list_filter = ["created_date", "published_date", "author"]
    search_fields = ["title", "article"]

    class Meta:
        model = Post

admin.site.register(Post, BlogAdmin)
