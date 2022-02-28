import imp
from django.urls import include, path,re_path
from .views import index
urlpatterns = [
    re_path(r'^.*/$',index),
    path("",index)
]
