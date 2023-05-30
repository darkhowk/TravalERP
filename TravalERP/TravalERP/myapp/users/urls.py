from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views


app_name = "users"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/', views.logout, name='logout'),
    path('changePw/', views.change_password.as_view(), name='password_change'),
]


