from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [    
    path("booking/", views.bookingIndex.as_view(), name="수배내역"), 
]
