from django.urls import path
from . import views

urlpatterns = [
    path('<str:req>', views.ApiView.as_view())
]