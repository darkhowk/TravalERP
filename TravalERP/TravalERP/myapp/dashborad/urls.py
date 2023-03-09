# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "dashborad"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("dashborad/", views.dashboradIndex.as_view(), name="dashborad_index"), 
]