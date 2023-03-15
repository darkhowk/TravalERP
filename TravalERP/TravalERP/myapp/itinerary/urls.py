# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "itinerary"

urlpatterns = [    
    path("itinerary/", views.itineraryIndex.as_view(), name="확정서"),
    path("itinerary/add/", views.itineraryAdd.as_view(), name="확정서추가"),
]