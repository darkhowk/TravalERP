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
    path("setting/agent", views.agentIndex.as_view(), name="여행사/로컬"), 
    path("setting/agent/addAgent", views.agentAdd.as_view(), name="여행사/로컬 등록/수정"), 
    path("setting/agent/addData", views.agentInsert, name="여생사/로컬 등록 ajax"), 
    path("setting/agent/updateData", views.agentModify, name="여행사/로컬 수정 ajax"), 
    path("setting/agent/deleteData", views.agentDelete, name="여행사/로컬 삭제 ajax"), 
    path("setting/manager", views.managerIndex.as_view(), name="담당자/로컬 담당자"), 
    path("setting/manager/addManager", views.managerAdd.as_view(), name="담당자/로컬 담당자 등록/수정"), 
    path("setting/manager/addData", views.managerInsert, name="담당자/로컬 담당자 등록 ajax"), 
    path("setting/manager/updateData", views.managerModify, name="담당자/로컬 담당자 수정 ajax"), 
    path("setting/manager/deleteData", views.managerDelete, name="담당자/로컬 담당자 삭제 ajax"), 
    path("setting/airport", views.airportIndex.as_view(), name="항공"), 
    path("setting/airport/addAirport", views.airportAdd.as_view(), name="항공 등록/수정"), 
    path("setting/airport/addData", views.airportInsert, name="항공 등록 ajax"), 
    path("setting/airport/updateData", views.airportModify, name="항공 수정 ajax"), 
    path("setting/airport/deleteData", views.airportDelete, name="항공 삭제 ajax"), 
]
