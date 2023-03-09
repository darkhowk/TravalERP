from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("setting/", views.settingList.as_view(), name="setting_list"), 
]
