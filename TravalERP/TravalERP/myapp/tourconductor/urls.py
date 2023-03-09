# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "tourconductor"

urlpatterns = [    
    path("tourconductor/", views.tourconductorIndex.as_view(), name="tourconductor_index"), 
]