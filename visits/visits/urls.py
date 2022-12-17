from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from visits import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('svisits/', include('svisits.urls')),
    path('api/', include('api.urls')),
]
