from django.urls import path
from svisits import views

urlpatterns = [
    path('<str:req>', views.index),
]
