# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "ton"

urlpatterns = [    
    path("ton/", views.tonproduct.as_view(), name="기술서"),


]  