from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^$', post_list),
        url(r'^create/$', post_create),
        url(r'^detail/$', post_detail),
        url(r'^update/$', post_update),
        url(r'^delete/$', post_delete),
]
