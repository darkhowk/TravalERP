# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "tourconductor"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("tourconductor/", views.tourconductorIndex.as_view(), name="tourconductor_index"), 
]