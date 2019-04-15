#tv_shows URL Configuration
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.watch.urls')),
]