from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * 
import json
# Create your views here.

class roomingIndex(generic.ListView):
   def __init__(self):
      self.title_nm = "루밍"
      self.ogImgUrl = ""
      self.descript = "루밍 페이지입니다"
      self.template_name = "rooming/index.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu
                     }

      return render(request, self.template_name, self.content)
   
class roomingAdd(generic.ListView):
   def __init__(self):
      self.title_nm = "루밍추가"
      self.ogImgUrl = ""
      self.descript = "루밍추가 페이지입니다"
      self.template_name = "rooming/add.html" 
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      tourconductor = Tourconductor.objects.filter(use_yn ='Y')
      optionData = {'tourconductor': tourconductor}
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "optionData" : optionData,
                     }

      return render(request, self.template_name, self.content)
   
def pathtoMode(path):
   if path == 'tourconductor':
      Models = Tourconductor
   return Models