import math
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from ..common.CommonView import CommonView, addView

from django.db.models.functions import Concat
from django.db.models import F, Value, CharField

from django.db.models.functions import Now

from ..common.common_models import *

# Create your views here.

#################################################
# INDEX
#################################################
class index(generic.ListView):
   def __init__(self):
        self.title_nm = "TON TOUR"
        self.ogImgUrl = ""
        self.descript = "TON TOUR 페이지입니다"
        self.template_name = "index.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP", use_yn = 'Y')
        self.leftMenu = Menu.objects.filter(menu_type="LEFT", use_yn = 'Y')
      
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "leftMenu"  : self.leftMenu
                     }

      return render(request, self.template_name, self.content)


#################################################
# SETTING
#################################################
class settingIndex(generic.ListView):
   def __init__(self):
        self.title_nm = "설정"
        self.ogImgUrl = ""
        self.descript = "설정 페이지입니다"
        self.template_name = "setting/index.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP")
        self.leftMenu = Menu.objects.filter(menu_type="LEFT")
      
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "leftMenu"  : self.leftMenu
                     }

      return render(request, self.template_name, self.content)


#################################################
# MENU
#################################################
class menuAdd(generic.ListView):
   def __init__(self):
        self.title_nm = "메뉴추가"
        self.ogImgUrl = ""
        self.descript = "메뉴추가 페이지입니다"
        self.template_name = "setting/menuAdd.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP")
        self.leftMenu = Menu.objects.filter(menu_type="LEFT")
      
   def get(self, request, *args, **kwargs):
      self.target = request.GET.get('target', None)
      if 'pageType' in request.GET:
         pageType = request.GET.get('pageType', None)
         self.perPage = request.GET.get('perPage', None)
         self.paging = request.GET.get('paging', None)
         if pageType == 'I':
            self.content = {
                           "descript" : self.descript,
                           "title_nm" : self.title_nm,
                           "ogImgUrl" : self.ogImgUrl,
                           "topMenu"  : self.topMenu,
                           "leftMenu" : self.leftMenu,
                           "pageType" : pageType,
                           "perPage"  : self.perPage,
                           "paging"   : self.paging,
                           "target"   : self.target,
                        }
         elif pageType == 'U':
            id = request.GET.get('id', None)
            self.contentMenu = Menu.objects.filter(id=id)
            self.content = {
                           "descript"    : self.descript,
                           "title_nm"    : self.title_nm,
                           "ogImgUrl"    : self.ogImgUrl,
                           "topMenu"     : self.topMenu,
                           "leftMenu"    : self.leftMenu,
                           "contentMenu" : self.contentMenu,
                           "pageType"    : pageType,
                           "perPage"     : self.perPage,
                           "paging"      : self.paging,
                            "target"   : self.target,
                        }
         

         return render(request, self.template_name, self.content)
      else :
         return render('', '/error', '')

#################################################
# AGENT
#################################################
class agentAdd(addView):
   def seletData(self):
      return {"agent": Agent.objects.filter(id=self.id, type = self.type)}
   
   def selectOption(self, request):
      return {}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/agentAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      self.type = request.GET.get('type', None)
      if self.pageType == 'I':
         if self.type == 'A':
            self.title_nm = "여행사 추가"
            self.descript = "여행사추가 페이지입니다"
         else :
            self.title_nm = "로컬 추가"
            self.descript = "로컬추가 페이지입니다"
      elif self.pageType == 'U':
         if self.type == 'A':
            self.title_nm = "여행사 수정"
            self.descript = "여행사 수정 페이지입니다"
         else :
            self.title_nm = "로컬 수정"
            self.descript = "로컬 수정 페이지입니다"
   
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response

#################################################
# MANAGER
#################################################
class managerAdd(addView):
   def seletData(self):
      return {'manager':Manager.objects.filter(id=self.id)}
   
   def selectOption(self, request):
      self.type = request.GET.get('type', None)
      if self.type == 'M':
         return {"agent":Agent.objects.filter(type="A", use_yn='Y')}
      else :
         return {"agent":Agent.objects.filter(type="L", use_yn='Y')}
      
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/managerAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      self.type = request.GET.get('type', None)

      if self.pageType == 'I':
         if self.type == 'M':
            self.title_nm = "담당자 추가"
            self.descript = "담당자추가 페이지입니다"
         else :
            self.title_nm = "로컬 담당자 추가"
            self.descript = "로컬 담당자 추가 페이지입니다"
            agent = Agent.objects.filter(type="L", use_yn='Y', )
      elif self.pageType == 'U':
         if self.type == 'M':
            self.title_nm = "담당자 수정"
            self.descript = "담당자 수정 페이지입니다"
         else :
            self.title_nm = "로컬 담당자 수정"
            self.descript = "로컬 담당자 수정 페이지입니다"

      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   

#################################################
# AIRPORT
#################################################
class airportAdd(addView):
   def seletData(self):
      return {"airport":Airport.objects.filter(id=self.id)}
   
   def selectOption(self, request):
      return {"citycode":Citycode.objects.filter(use_yn='Y')}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/airportAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      if self.pageType == 'I':
            self.title_nm = "항공 추가"
            self.descript = "항공 추가 페이지입니다"
      elif self.pageType == 'U':
            self.title_nm = "항공 수정"
            self.descript = "항공 수정 페이지입니다"

      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   
#################################################
# BANK
#################################################
class bankAdd(addView):
   def seletData(self):
      return {"bank":Bank.objects.filter(id=self.id)}
   
   def selectOption(self, request):
      return {}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/bankAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      if self.pageType == 'I':
            self.title_nm = "은행 추가"
            self.descript = "은행 추가 페이지입니다"
      elif self.pageType == 'U':
            self.title_nm = "은행 수정"
            self.descript = "은행 수정 페이지입니다"
      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   
#################################################
# COMMCODE
#################################################
class commcodeAdd(addView):
   def seletData(self):
      return {"commcode":CommCode.objects.filter(id=self.id)}
   
   def selectOption(self, request):
      return {}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/commcodeAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      if self.pageType == 'I':
            self.title_nm = "공통코드 추가"
            self.descript = "공통코드 추가 페이지입니다"
      elif self.pageType == 'U':
            self.title_nm = "공통코드 수정"
            self.descript = "공통코드 수정 페이지입니다"
      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   
#################################################
# HOTEL
#################################################
class hotelAdd(addView):
   def seletData(self):
      return {"hotel":Hotel.objects.filter(id=self.id)}
   
   def selectOption(self, request):
      return {"citycode":Citycode.objects.filter(use_yn='Y')}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/hotelAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      if self.pageType == 'I':
            self.title_nm = "호텔 추가"
            self.descript = "호텔 추가 페이지입니다"
      elif self.pageType == 'U':
            self.title_nm = "호텔 수정"
            self.descript = "호텔 수정 페이지입니다"
      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   
   
   
#################################################
# SCHEDULE
#################################################
class scheduleAdd(addView):
   def seletData(self):
      return {"scheduleMaster":ScheduleMaster.objects.filter(id=self.id),"scheduleDetail": ScheduleDetail.objects.filter(master_id=self.id)}
   
   def selectOption(self, request):
      return {'agent':Agent.objects.filter(use_yn='Y',type='A')}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/scheduleAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      if self.pageType == 'I':
            self.title_nm = "스케줄 추가"
            self.descript = "스케쥴 추가 페이지입니다"
      elif self.pageType == 'U':
            self.title_nm = "스케줄 수정"
            self.descript = "스케줄 수정 페이지입니다"
      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   

#################################################
# CITYCODE
#################################################
class citycodeAdd(addView):
   def seletData(self):
      return {"citycode":Citycode.objects.filter(id=self.id)}
   
   def selectOption(self, request):
      return {}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/citycodeAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      if self.pageType == 'I':
            self.title_nm = "도시코드 추가"
            self.descript = "도시코드 추가 페이지입니다"
      elif self.pageType == 'U':
            self.title_nm = "도시코드 수정"
            self.descript = "도시코드 수정 페이지입니다"
      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response    
   


#################################################
# T/C
#################################################
class tourconductorAdd(addView):
   def seletData(self):
      return {"tourconductor":Tourconductor.objects.filter(id=self.id)}
   
   def selectOption(self, request):
      return {}
   
   def get(self, request, *args, **kwargs):
      self.template_name = "setting/tourconductorAdd.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      if self.pageType == 'I':
            self.title_nm = "T/C 추가"
            self.descript = "T/C 추가 페이지입니다"
      elif self.pageType == 'U':
            self.title_nm = "T/C 수정"
            self.descript = "T/C 수정 페이지입니다"
      
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response

#################################################
# Common Setting View ( 공통 List 화면 View)
#################################################
class commonSettingView(CommonView):
   def custom_queryset(self):
      if self.target == 'airport':
         self.title_nm='항공'
         self.descript = '항공 등록 페이지입니다.'
         return  Airport, None, None
      
      if self.target ==  'manager':
         if self.type == 'M':
            self.title_nm = "담당자"
            self.descript = "담당자 페이지입니다"
         else :
            self.title_nm = "로컬 담당자"
            self.descript = "로컬 담당자 페이지입니다"
         return Manager, 'type', self.type

      if self.target == 'agent':
         if self.type == 'A':
            self.title_nm = "여행사"
            self.descript = "여행사 관리 페이지입니다"  
         else :
            self.title_nm = "로컬"
            self.descript = "로컬 관리 페이지입니다"
         return Agent, 'type', self.type

      if self.target == 'menu':
         self.title_nm = "메뉴관리"
         self.descript = "메뉴관리 페이지입니다"
         return Menu, None, None
      
      if self.target == 'commcode':
         self.title_nm = "공통코드"
         self.descript = "공통코드 페이지입니다"
         return CommCode, None, None
      
      if self.target == 'schedule':
         self.title_nm = "스케쥴관리"
         self.descript = "스케쥴관리 페이지입니다"
         return ScheduleMaster, None, None
      
      if self.target == 'hotel':
         self.title_nm = "호텔"
         self.descript = "호텔 페이지입니다"
         return Hotel, None, None

      if self.target == 'bank':
         self.title_nm = "은행"
         self.descript = "은행 페이지입니다"
         return Bank, None, None
      
      if self.target == 'citycode':
         self.title_nm = "도시코드"
         self.descript = "도시코드 페이지입니다"
         return Citycode, None, None
      
      if self.target == 'tourconductor':
         self.title_nm = "T/C"
         self.descript = "T/C 페이지입니다"
         return Tourconductor, None, None
      
      

   def get(self, request, *args, **kwargs):
      self.type = request.GET.get('type')
      self.target = request.GET.get('target')
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   




   

#################################################
# Common Path별 Model선택
#################################################
def pathtoMode(path):
   print(path)
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
   if path == 'tourconductor':
      Models = Tourconductor
   return Models
