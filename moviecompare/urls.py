from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.search_movie, name='compare'),
    url(r'^movies/$', views.search_movie, name='movies')
]
