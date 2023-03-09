from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("", views.index.as_view(), name="메인페이지"),
    path("setting/", views.settingIndex.as_view(), name="설정"), 
    path("setting/menu", views.settingMenu.as_view(), name="메뉴관리"), 
]
