from django.urls import path, include, re_path
#from django.conf.urls import urls
from svisits import views


from .views import *

urlpatterns = [
    re_path(r'^Student$', views.StudentApi),
    re_path(r'^Student/([0-1000]+)$', views.StudentApi),
]
