# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "invoice"

urlpatterns = [    
    path("invoice/", views.invoiceIndex.as_view(), name="인보이스"), 
]