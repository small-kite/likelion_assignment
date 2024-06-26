from django.urls import path
from .views import *


urlpatterns = [
  path('signup/', signup, name='signup'),
  path('login/', signup, name='login'),
  path('logout/', signup, name='logout'),
]
