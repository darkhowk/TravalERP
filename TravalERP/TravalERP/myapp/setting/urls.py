from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    path("", views.index.as_view(), name="메인페이지"),
    path("setting/", views.settingIndex.as_view(), name="설정"), 
    path("setting/menu", views.settingMenu.as_view(), name="메뉴관리"), 
    path("setting/menu/addMenu", views.menuAdd.as_view(), name="메뉴 등록/수정"), 
    path("setting/menu/addData", views.menuInsert, name="메뉴등록 ajax"), 
    path("setting/menu/updateData", views.menuModify, name="메뉴수정 ajax"), 
    path("setting/menu/deleteData", views.menuDelete, name="메뉴삭제 ajax"), 
    path("setting/agent", views.agentIndex.as_view(), name="여행사"), 
    path("setting/agent/addAgent", views.agentAdd.as_view(), name="여행사 등록/수정"), 
    path("setting/agent/addData", views.agentInsert, name="여생사등록 ajax"), 
    path("setting/agent/updateData", views.agentModify, name="여행사 수정 ajax"), 
    path("setting/agent/deleteData", views.agentDelete, name="여행사 삭제 ajax"), 
   
]
