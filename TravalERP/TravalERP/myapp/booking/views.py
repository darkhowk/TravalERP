from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
# from ..common.common_models import Menu # 기존 Menu만 불러오던걸 주석
from ..common.common_models import * # 모든 모델 가져올수있게 변경
import json
# Create your views here.

class bookingIndex(generic.ListView):
   def __init__(self):
      self.title_nm = "수배내역"
      self.ogImgUrl = ""
      self.descript = "수배내역 페이지입니다"
      self.template_name = "booking/index.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu
                     }

      return render(request, self.template_name, self.content)
   
class bookingAdd(generic.ListView):
   def __init__(self):
      self.title_nm = "수배추가"
      self.ogImgUrl = "" 
      self.descript = "수배추가 페이지입니다"
      self.template_name = "booking/add.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      # 추가할 데이터
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