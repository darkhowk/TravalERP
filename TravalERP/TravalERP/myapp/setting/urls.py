from django.urls import path
from . import views

app_name = "setting"

urlpatterns = [    
    #전체 index 페이지
    path("", views.index.as_view(), name="메인페이지"),

    #설정 index페이지
    path("setting/", views.settingIndex.as_view(), name="설정"), 

    ##설정 상세 페이지(등록/수정)
    path("setting/menu/add", views.menuAdd.as_view(), name="메뉴 등록/수정"), 
    path("setting/agent/add", views.agentAdd.as_view(), name="여행사/로컬 등록/수정"),  
    path("setting/manager/add", views.managerAdd.as_view(), name="담당자/로컬 담당자 등록/수정"), 
    path("setting/airport/add", views.airportAdd.as_view(), name="항공 등록/수정"), 
    
    ### 공통 List View
    path("setting/commonSettingView", views.commonSettingView.as_view(), name="공통 List 화면"), 

    #### 공통 ajax
    path("setting/<str:path>/addData", views.commonInsert, name="공통등록 ajax"),
    path("setting/<str:path>/updateData", views.commonModify, name="공통수정 ajax"),
    path("setting/<str:path>/deleteData", views.commonDelete, name="공통삭제 ajax"),

]
