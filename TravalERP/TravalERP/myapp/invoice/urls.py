# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "invoice"

urlpatterns = [    
    path("", views.firstIndex.as_view(), name="first_index"), 
    path("invoice/", views.invoiceIndex.as_view(), name="invoice_index"), 
]