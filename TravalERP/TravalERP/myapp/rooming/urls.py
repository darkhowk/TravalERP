# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "rooming"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("rooming/", views.roomingIndex.as_view(), name="rooming_index"), 
]