# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "statement"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("statement/", views.statementIndex.as_view(), name="statement_index"), 
]