# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "rooming"

urlpatterns = [    
    path("rooming/", views.roomingIndex.as_view(), name="rooming_index"), 
]