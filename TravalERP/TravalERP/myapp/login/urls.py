from django.urls import path
from . import views

app_name = "login"

urlpatterns = [    
    path("login/", views.loginIndex.as_view(), name="로그인"),
    path("login/pwr/", views.loginPwr.as_view(), name="패스워드"),
]