from django.urls import path

from .views import point

urlpatterns = [
    path('', point, name='home')
]