from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.create_user, name='create_user'),
    path('login/',views.login, name='login'),
]