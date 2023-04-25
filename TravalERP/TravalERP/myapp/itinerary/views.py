from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..itinerary.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView
# Create your views here.

class itineraryIndex(CommonMainView): 

   def custom_queryset(self):
      return  ItineraryMaster, None, None
   

   def get(self, request, *args, **kwargs):
      self.title_nm = "ITINERARY LIST"
      self.descript = "확정서 페이지입니다"
      self.template_name = "itinerary/index.html"
      self.target = "itinerary"
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response 



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
      tourconductor = Tourconductor.objects.filter(use_yn ='Y')
      master = ItineraryMaster.objects.filter(id=request.GET.get('id'))
      detail = ItineraryDetail.objects.filter(itinerary_id=request.GET.get('id'))
      selectData = {'master': master,'detail':detail}
      optionData = {'localAgent' : localAgent, 'localTel' : localTel, 'manager' : manager, 'localManager' : localManager, 'tourconductor': tourconductor} # 추후 추가할 데이터를 위해
      target = 'itinerary'
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "optionData" : optionData,
                        "selectData" : selectData,
                        "target" : target,
                     }

      return render(request, self.template_name, self.content) 
   


def pathtoMode(path):
   if path == 'tourconductor':
      Models = Tourconductor