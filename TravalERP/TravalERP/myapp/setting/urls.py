from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("", views.index.as_view(), name="메인페이지"),
    path("setting/", views.settingIndex.as_view(), name="설정"), 
    path("setting/menu", views.settingMenu.as_view(), name="메뉴관리"), 
    path("setting/menu/addMenu", views.settingAddMenu.as_view(), name="메뉴추가"), 
    path("setting/menu/addData", views.settingMenuInsert, name="메뉴추가 ajax"), 
    path("setting/menu/updateData", views.settingMenuModify, name="메뉴수정 ajax"), 
    path("setting/menu/deleteData", views.settingMenuDelete, name="메뉴삭제 ajax"), 
]
