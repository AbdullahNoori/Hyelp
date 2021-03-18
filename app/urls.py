from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('detail/', detail, name='detail'),
]