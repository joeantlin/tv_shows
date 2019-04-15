from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/(?P<showid>\d+)$', views.showpage),
    url(r'^shows/(?P<editid>\d+)/edit$', views.editpage),
    url(r'^shows/edit$', views.editedshow),
    url(r'^shows/create$', views.createpage),
    url(r'^shows/newshow$', views.newshow),
    url(r'^shows/delete/(?P<deleteid>\d+)$', views.deleteshow),
]