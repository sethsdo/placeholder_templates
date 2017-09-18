from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^blogs/$', views.index),     # This line has changed!
    url(r'^new/$', views.newform),
    url(r'^create/$', views.createBlog),
    url(r'^(\d+)/$', views.number),
    url(r'^(\d+)/edit/$', views.edit),
    url(r'^(\d+)/delete/$', views.delete),
    url(r'^(\d+)/distroy/$', views.distroy),
]

