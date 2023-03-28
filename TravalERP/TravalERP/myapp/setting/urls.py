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

    
    
    ## 공통 List View
    path("setting/commonSettingView", views.commonSettingView.as_view(), name="공통 List 화면"), 

    ### 공통 copy Data
    path("setting/copyData", views.commonCopy, name="데이터 카피 ajax"),

    #### 공통 ajax
    path("setting/<str:path>/addData", views.commonInsert, name="공통등록 ajax"),
    path("setting/<str:path>/updateData", views.commonModify, name="공통수정 ajax"),
    path("setting/<str:path>/deleteData", views.commonDelete, name="공통삭제 ajax"),

    ##### Master Detail ajax
    path("setting/<str:path>/addDataMaster", views.commonInsertMaster, name="공통 master등록 ajax"),
    path("setting/<str:path>/addDataDetail", views.commonInsertDetail, name="공통 detail등록 ajax"),
    path("setting/<str:path>/updateDataMaster", views.commonModifyMaster, name="공통 master등록수정 ajax"),
    path("setting/<str:path>/updateDataDetail", views.commonModifyDetail, name="공통 detail등록수정 ajax"),
    path("setting/<str:path>/deleteDataMaster", views.commonDeleteMaster, name="공통 master등록삭제 ajax"),
    path("setting/<str:path>/deleteDataDetail", views.commonDeleteDetail, name="공통 detail등록삭제 ajax"),

    ###### ajax get Data 
    path("setting/<str:path>/getAjax/<str:item>", views.commonGetAjaxData, name='공통 ajax 데이터' )
]
