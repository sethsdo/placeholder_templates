from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^register/$', views.register),     # This line has changed!
    url(r'^login/$', views.login),
    url(r'^new/$', views.newUser),
    url(r'^users/$', views.users),
]
