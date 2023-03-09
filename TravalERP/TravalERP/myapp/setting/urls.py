from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("setting/", views.settingIndex.as_view(), name="설정"), 
]
