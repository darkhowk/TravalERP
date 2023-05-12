from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..itinerary.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView, CommonMainAddView
# Create your views here.

class itineraryIndex(CommonMainView): 

   def custom_queryset(self):
      return  ItineraryMaster.objects.filter(use_yn='Y')
   

   def get(self, request, *args, **kwargs):
      self.title_nm = "ITINERARY LIST"
      self.descript = "확정서 페이지입니다"
      self.template_name = "itinerary/index.html"
      self.target = "itinerary"
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response 


class itineraryAdd(CommonMainAddView):

   def seletData(self):
      return { "master" : ItineraryMaster.objects.filter(id=self.id),
               "detail" : ItineraryDetail.objects.filter(itinerary_id=self.id),
            }
   
   def selectOption(self, request):
      return {  }
   
   def get(self, request, *args, **kwargs):
      self.template_name = "itinerary/add.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      self.type = request.GET.get('type', None)

      if self.pageType == 'I':
         self.title_nm = "확정서추가"
         self.descript = "확정서추가 페이지입니다"
      elif self.pageType == 'U':
         self.title_nm = "확정서수정"
         self.descript = "확정서수정 페이지입니다"

      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response