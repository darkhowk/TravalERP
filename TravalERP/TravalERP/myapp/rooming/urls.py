# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "rooming"

urlpatterns = [    
    path("rooming/", views.roomingIndex.as_view(), name="루밍"),
    path("rooming/add/", views.roomingAdd.as_view(), name="루밍추가"), 
]