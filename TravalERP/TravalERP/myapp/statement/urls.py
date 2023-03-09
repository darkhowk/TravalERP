# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "statement"

urlpatterns = [    
    path("statement/", views.statementIndex.as_view(), name="정산"), 
]