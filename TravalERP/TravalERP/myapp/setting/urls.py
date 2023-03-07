from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("setting.do", views.index.as_view(), name="setting"),
]