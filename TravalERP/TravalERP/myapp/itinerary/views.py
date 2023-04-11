from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * 
import json

class itineraryIndex(generic.ListView):
   def __init__(self):
      self.title_nm = "확정서"
      self.ogImgUrl = ""
      self.descript = "확정서 페이지입니다"
      self.template_name = "itinerary/index.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu
                     }

      return render(request, self.template_name, self.content)
   
class itineraryAdd(generic.ListView):
   def __init__(self):
      self.title_nm = "확정서추가"
      self.ogImgUrl = ""
      self.descript = "확정서추가 페이지입니다"
      self.template_name = "itinerary/add.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      localAgent = Agent.objects.filter(use_yn ='Y', type='L')
      localTel = Agent.objects.filter(use_yn ='Y', agent_tel='')
      manager = Manager.objects.filter(use_yn ='Y', type='M')
      localManager = Manager.objects.filter(use_yn ='Y', type='L')
      optionData = {'localAgent' : localAgent, 'localTel' : localTel, 'manager' : manager, 'localManager' : localManager} # 추후 추가할 데이터를 위해
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "optionData" : optionData,
                     }

      return render(request, self.template_name, self.content)
   