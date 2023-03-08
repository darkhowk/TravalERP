from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path('setting/', views.settingList.as_view(), name='setting_list'), 
]
