from django.urls import path, include
from core.views import *

urlpatterns = [
    path('', index),
]
