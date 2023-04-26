from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..booking.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView, CommonMainAddView
# Create your views here.

class bookingIndex(CommonMainView):

   def custom_queryset(self):
      return  BookingMaster, None, None
        
   def get(self, request, *args, **kwargs):
      self.title_nm = "BOOKING LIST"
      self.descript = "수배내역 페이지입니다"
      self.template_name = "booking/index.html"
      self.target = "booking"
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   
class bookingAdd(CommonMainAddView):

   def seletData(self):
      return { "master" : BookingMaster.objects.filter(id=self.id),
               "detail" : BookingDetail.objects.filter(booking_id=self.id),
            }
   
   def selectOption(self, request):
      return { "agent"        : Agent.objects.filter(use_yn ='Y', type='A'),
               "localAgent"   : Agent.objects.filter(use_yn ='Y', type='L'),
               "manager"      : Manager.objects.filter(use_yn ='Y', type='M'),
               "localManager" : Manager.objects.filter(use_yn ='Y', type='L'),
               "airport"      : Airport.objects.filter(use_yn ='Y'),
            }
   
   
   def get(self, request, *args, **kwargs):
      self.template_name = "booking/add.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      self.type = request.GET.get('type', None)

      if self.pageType == 'I':
         self.title_nm = "수배 추가"
         self.descript = "수배추가 페이지입니다"
      elif self.pageType == 'U':
         self.title_nm = "수배 수정"
         self.descript = "수배수정 페이지입니다"

   
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response

def commonGetAjaxData(request, path, item):
   Models = pathtoMode(item)

   data = request.body.decode('utf-8')

   try:
      # JSON 형식으로 변환
      params = json.loads(data)
      data = list(Models.objects.filter(**params).values())
      return JsonResponse(data, safe=False)
      # JSON 형식이 맞는 경우 처리할 코드
   except json.decoder.JSONDecodeError:
        # JSON 형식이 아닌 경우 처리할 코드
      return JsonResponse(data, safe=False)
  
def pathtoMode(path):
   if path == 'agent':
      Models = Agent
   if path == 'airport':
      Models = Airport
   if path == 'bank':
      Models = Bank
   if path == 'commcode':
      Models = CommCode
   if path == 'hotel':
      Models = Hotel
   if path == 'manager':
      Models = Manager
   if path == 'menu':
      Models = Menu
   if path == 'scheduleMaster':
      Models = ScheduleMaster
   if path == 'scheduleDetail':
      Models = ScheduleDetail
   if path == 'citycode':
      Models = Citycode
   return Models

def bookingSearch(request):
    return render(request, 'booking/search.html')