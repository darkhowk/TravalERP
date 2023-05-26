from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/', views.logout, name='logout'),
    path('changePw/', views.change_password, name="change_password"),
]