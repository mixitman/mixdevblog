from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]

    search_fields = ["title", "content"]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)


# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/