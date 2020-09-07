from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('check/k/', check_keyword),
    path('image/', session_image)
]
