from django.urls import path
from .views import home

# 127.0.0.1/blog/

urlpatterns = [
    
    path('', home),
]

