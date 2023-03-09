# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "itinerary"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("itinerary/", views.itineraryIndex.as_view(), name="itinerary_index"), 
]