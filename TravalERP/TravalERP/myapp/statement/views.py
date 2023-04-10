from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import *
import json

class statementIndex(generic.ListView): 
   def __init__(self):
        self.title_nm = "정산"
        self.ogImgUrl = ""
        self.descript = "정산 페이지입니다"
        self.template_name = "statement/index.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP")

      
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                     }

      return render(request, self.template_name, self.content)
   
class statementAdd(generic.ListView):
   def __init__(self):
      self.title_nm = "정산추가"
      self.ogImgUrl = ""
      self.descript = "정산추가 페이지입니다"
      self.template_name = "statement/add.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      agent = Agent.objects.filter(use_yn ='Y', type='A') # 사용여부 Y, 타입 A(여행사) 인것 선택
      localAgent = Agent.objects.filter(use_yn ='Y', type='L')
      manager = Manager.objects.filter(use_yn ='Y', type='M')
      localManager = Manager.objects.filter(use_yn ='Y', type='L')
      airport = Airport.objects.filter(use_yn ='Y')
      optionData = {'agent': agent, 'localAgent' : localAgent, 'manager' : manager, 'localManager' : localManager, 'airport' : airport} # 추후 추가할 데이터를 위해
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "optionData" : optionData,
                     }

      return render(request, self.template_name, self.content) 
