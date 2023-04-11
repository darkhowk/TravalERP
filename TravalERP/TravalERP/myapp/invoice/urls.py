# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "invoice"

urlpatterns = [    
    path("invoice/", views.invoiceIndex.as_view(), name="인보이스"),
    path("invoice/add/", views.invoiceAdd.as_view(), name="인보이스추가"), 
    path("invoice/search/", views.invoiceSearch, name="일정 검색"), 
] 