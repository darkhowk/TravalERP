from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("booking/", views.bookingIndex.as_view(), name="booking_index"), 
]
