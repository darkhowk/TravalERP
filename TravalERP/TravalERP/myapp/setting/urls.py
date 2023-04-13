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
    path("setting/bank/add", views.bankAdd.as_view(), name="은행 등록/수정"), 
    path("setting/commcode/add", views.commcodeAdd.as_view(), name="공통코드 등록/수정"), 
    path("setting/hotel/add", views.hotelAdd.as_view(), name="호텔 등록/수정"), 
    path("setting/schedule/add", views.scheduleAdd.as_view(), name="스케줄 등록/수정"), 
    path("setting/citycode/add", views.citycodeAdd.as_view(), name="도시코드 등록/수정"), 
    path("setting/tourconductor/add", views.tourconductorAdd.as_view(), name="T/C 등록/수정"), 

    
    
    ## 공통 List View
    path("setting/commonSettingView", views.commonSettingView.as_view(), name="공통 List 화면"), 

   ]
