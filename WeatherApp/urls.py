from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('weather/', include('weather.urls')),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
]
