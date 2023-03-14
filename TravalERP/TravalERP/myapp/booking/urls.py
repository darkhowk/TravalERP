from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [    
    path("booking/", views.bookingIndex.as_view(), name="수배내역"), 
    path("booking/add/", views.bookingAdd.as_view(), name="수배추가"), 
    path("booking/add2/", views.bookingAdd2.as_view(), name="수배추가2"), 
     path("booking/addModify/", views.bookingAddModify.as_view(), name="수배추가2"), 
]
