from django.conf.urls import url
# from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success/(?P<id>\d+)$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^addreview/(?P<id>\d+)$', views.addreview),
    url(r'^booked/(?P<id>\d+)$', views.booked),
    url(r'^return$', views.account)
    # url(r'^addreview/(?P<id>\d+)$', views.addreview),  #TODO
]
