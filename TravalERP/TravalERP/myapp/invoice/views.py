from django.shortcuts import render
from django.views import generic
from .models import Menu
# Create your views here.

class invoiceIndex(generic.ListView):
   model = Menu
    