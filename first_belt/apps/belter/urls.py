from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success/(?P<id>\d+)$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^return$', views.account),
    url(r'^(?P<word>.+)$', views.nein)
]
