from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<title>[\w\s]+)/$', views.post_detail),
    url(r'^categoria/(?P<nome>[\w\s]+)/$', views.category_posts),
]