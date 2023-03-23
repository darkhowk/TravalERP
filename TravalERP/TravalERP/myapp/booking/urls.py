from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [    
    path("booking/", views.bookingIndex.as_view(), name="수배내역"), 
    path("booking/add/", views.bookingAdd.as_view(), name="수배추가"), 
    ###### ajax get Data 
    path("booking/<str:path>/getAjax/<str:item>", views.commonGetAjaxData, name='공통 ajax 데이터' )

]
