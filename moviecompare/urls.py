from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<movid>[0-9]+)$', views.get_movie, name='movie_detail'),
    url(r'^', views.search_movie, name='compare'),
]

