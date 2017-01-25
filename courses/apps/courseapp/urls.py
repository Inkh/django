from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.addition),
    url(r'^destroy/(?P<jim>\d+)$', views.destroy),
    url(r'^demolish/(?P<jim>\d+)$', views.demolish)
]
