from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("setting/", views.settingIndex.as_view(), name="setting_index"), 
]
