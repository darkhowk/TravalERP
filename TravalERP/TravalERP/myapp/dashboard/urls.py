# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [     
    path("dashboard/", views.dashboardIndex.as_view(), name="대시보드"), 
]