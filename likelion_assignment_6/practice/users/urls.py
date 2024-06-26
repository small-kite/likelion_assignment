from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/<int:user_id>/profile_edit/', views.profile_edit, name='profile_edit'),
    path('users/<int:user_id>/profile_base/', views.profile_base, name='profile_base'),
    


]

