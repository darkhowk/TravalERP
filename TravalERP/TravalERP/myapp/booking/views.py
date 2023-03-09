from django.shortcuts import render
from django.views import generic
from .models import Menu
# Create your views here.

class bookingIndex(generic.ListView):
    model = Menu
    