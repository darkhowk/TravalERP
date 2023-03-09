from django.shortcuts import render
from django.views import generic

from .models import Menu, Users
# Create your views here.

class settingList(generic.ListView):
    model = Menu