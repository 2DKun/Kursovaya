
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('svisits/', include('svisits.urls')),
    path('api/', include('api.urls')),
]
