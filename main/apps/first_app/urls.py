# print "I will be your future routes; HTTP requests will be captured by me. "
from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^users$', views.show)
]
