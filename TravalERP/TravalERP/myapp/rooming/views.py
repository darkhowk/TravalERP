from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..rooming.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView, CommonMainAddView
# Create your views here.

class roomingIndex(CommonMainView):

   def custom_queryset(self):
      return  RoomingMaster.objects.filter(use_yn='Y')

   def get(self, request, *args, **kwargs):
      self.title_nm = "ROOMING LIST"
      self.descript = "루밍리스트 페이지입니다"
      self.template_name = "rooming/index.html"
      self.target = "rooming"
      response = super().get(request, *args, **kwargs) 
      
      if response is None:
         response = HttpResponse()
         
      return response 
   

class roomingAdd(CommonMainAddView):

   def seletData(self):
      return { "master" : RoomingMaster.objects.filter(id=self.id),
               "detail" : RoomingDetail.objects.filter(rooming_id=self.id),
            }
   
   def selectOption(self, request):
      return { "tourconductor" : Tourconductor.objects.filter(use_yn ='Y'),
            }
   
   def get(self, request, *args, **kwargs):
      self.template_name = "rooming/add.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      self.type = request.GET.get('type', None)

      if self.pageType == 'I':
         self.title_nm = "루밍추가"
         self.descript = "루밍추가 페이지입니다"
      elif self.pageType == 'U':
         self.title_nm = "루밍수정"
         self.descript = "루밍수정 페이지입니다"

      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
