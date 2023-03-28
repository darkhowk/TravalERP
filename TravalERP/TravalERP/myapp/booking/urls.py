from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [    
    path("booking/", views.bookingIndex.as_view(), name="수배내역"), 
    path("booking/add/", views.bookingAdd.as_view(), name="수배추가"), 
    path("booking/search/", views.bookingSearch, name="일정 검색"), 
    ###### ajax get Data 
    path("booking/<str:path>/getAjax/<str:item>", views.commonGetAjaxData, name='공통 ajax 데이터' )

]
