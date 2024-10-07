from django.urls import path
from .views import index, profile_view, register, index1, get_csrf

urlpatterns = [
    # path('', index),
    path('home/', index1),
    path('profile/', profile_view, name="profile"),
    path('register/', register, name="register"),
    path('csrf/', get_csrf, name='api-csrf'),
]

