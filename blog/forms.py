from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "featured_image",
            "article",
            "author",
            "draft",
            "published_date",
        ]
