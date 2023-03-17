import math
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from ..common.CommonView import CommonView, addView
import datetime

from ..common.common_models import Menu, Agent, Manager, Airport

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
class agentAdd(generic.ListView):
   def __init__(self):
        self.title_nm = "여행사 추가"
        self.descript = "여행사추가 페이지입니다"
        self.template_name = "setting/agentAdd.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP")
        self.leftMenu = Menu.objects.filter(menu_type="LEFT")
      
   def get(self, request, *args, **kwargs):
      pageType = request.GET.get('pageType', None)
      type = request.GET.get('type', None)
      target = request.GET.get('target', None)
      if pageType == 'I':
         if type == 'A':
            self.title_nm = "여행사 추가"
            self.descript = "여행사추가 페이지입니다"
         else :
            self.title_nm = "로컬 추가"
            self.descript = "로컬추가 페이지입니다"

         self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "topMenu"  : self.topMenu,
                        "leftMenu" : self.leftMenu,
                        "pageType" : pageType,
                        "type" : type,
                        "target" : target,
                     }
      elif pageType == 'U':
         type = request.GET.get('type', None)
         if type == 'A':
            self.title_nm = "여행사 수정"
            self.descript = "여행사 수정 페이지입니다"
         else :
            self.title_nm = "로컬 수정"
            self.descript = "로컬 수정 페이지입니다"

         id =  request.GET.get('id', None)
         self.agent = Agent.objects.filter(id=id, type = type)
         self.perPage = request.GET.get('perPage', None)
         self.paging = request.GET.get('paging', None)
         self.content = {
                        "descript"    : self.descript,
                        "title_nm"    : self.title_nm,
                        "topMenu"     : self.topMenu,
                        "leftMenu"    : self.leftMenu,
                        "pageType"    : pageType,
                        "perPage"     : self.perPage,
                        "paging"      : self.paging,
                        "type"         : type,
                        "agent"       : self.agent,
                        "target"       : target,
                     }
      return render(request, self.template_name, self.content)

#################################################
# MANAGER
#################################################
class managerAdd(generic.ListView):
   def __init__(self):
        self.title_nm = "담당자 추가"
        self.ogImgUrl = ""
        self.descript = "담당자추가 페이지입니다"
        self.template_name = "setting/managerAdd.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP")
        self.leftMenu = Menu.objects.filter(menu_type="LEFT")
      
   def get(self, request, *args, **kwargs):
      perPage = request.GET.get('perPage', None)
      paging = request.GET.get('paging', None)
      target = request.GET.get('target', None)
      pageType = request.GET.get('pageType', None)
      type = request.GET.get('type', None)

      if pageType == 'I':
         if type == 'M':
            self.title_nm = "담당자 추가"
            self.descript = "담당자추가 페이지입니다"
            agent = Agent.objects.filter(type="A", use_yn='Y', )
         else :
            self.title_nm = "로컬 담당자 추가"
            self.descript = "로컬 담당자 추가 페이지입니다"
            agent = Agent.objects.filter(type="L", use_yn='Y', )

         self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "leftMenu" : self.leftMenu,
                        "pageType" : pageType,
                        "type" : type,
                        "agent": agent,
                        "perPage": perPage,
                        "paging": paging,
                        "target": target,
                     }
      elif pageType == 'U':
         type = request.GET.get('type', None)
         if type == 'M':
            self.title_nm = "담당자 수정"
            self.descript = "담당자 수정 페이지입니다"
            agent = Agent.objects.filter(agent_type="A", use_yn='Y', )
         else :
            self.title_nm = "로컬 담당자 수정"
            self.descript = "로컬 담당자 수정 페이지입니다"
            agent = Agent.objects.filter(agent_type="L", use_yn='Y', )

         id =  request.GET.get('id', None)
         self.manager = Manager.objects.filter(id=id, type = type)
         self.perPage = request.GET.get('perPage', None)
         self.paging = request.GET.get('paging', None)
         self.content = {
                        "descript"    : self.descript,
                        "title_nm"    : self.title_nm,
                        "ogImgUrl"    : self.ogImgUrl,
                        "topMenu"     : self.topMenu,
                        "leftMenu"    : self.leftMenu,
                        "pageType"    : pageType,
                        "perPage"     : self.perPage,
                        "paging"      : self.paging,
                        "type"        : type,
                        "manager"     : self.manager,
                        "agent": agent,
                     }
      return render(request, self.template_name, self.content)

#################################################
# AIRPORT
#################################################
class airportAdd(addView):
   def seletData(self):
      return Airport.objects.filter(id=self.id)
   
   def selectOption(self, request):
      return {'manager':Manager.objects.filter(use_yn='Y')}
   
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
# Common Setting View ( 공통 List 화면 View)
#################################################
class commonSettingView(CommonView):
   def custom_queryset(self):
      if self.target == 'airport':
         self.title_nm='항공'
         self.descript = '항동 등록 페이지입니다.'
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
      
      if self.target == 'schdule':
         self.title_nm = "스케쥴관리"
         self.descript = "스케쥴관리 페이지입니다"
         return Menu, None, None

   def get(self, request, *args, **kwargs):
      self.type = request.GET.get('type')
      self.target = request.GET.get('target')
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response
   

def commonInsert(request, path):
   # model별로 insert할 fields 작성
   fields = []
   Models = None

   print(path)
   if path == 'manager':
      Models = Manager
   if path == 'agent':
      Models = Agent
   if path == 'menu':
      Models = Menu
   if path == 'airport':
      Models = Airport
   
   fields = [f.name for f in Models._meta.fields if f.name not in ['entry_date', 'entry_id', 'updat_date', 'updat_id', 'id']]

   return insert(request, Models, fields)

def insert(request, model, fields):
    now = datetime.datetime.now()

    data = {}
    for field in fields:
        data[field] = request.POST.get(field)

    model_instance = model(**data, entry_date=now.strftime('%Y-%m-%d %H:%M:%S'))
    model_instance.save()

    return JsonResponse({'result': 'success'})

def commonModify(request, path):
   Models = None

   if path == 'manager':
      Models = Manager
   if path == 'agent':
      Models = Agent
   if path == 'menu':
      Models = Menu
   if path == 'airport':
      Models = Airport

   type = request.POST.get('type', None)

   if type is None:
      print('modift none')
      return modify(request, Models)
   else: 
      return modify(request, Models, pk_name='id', type=type)

def commonDelete(request, path):
   Models = None

   print(path)
   if path == 'manager':
      Models = Manager
   if path == 'agent':
      Models = Agent
   if path == 'menu':
      Models = Menu
   if path == 'airport':
      Models = Airport

   type = request.POST.get('type', None)
   if type is None:
      return delete(request, Models)
   else: 
      return delete(request, Models, pk_name='id', type=type)

def modify(request, model, pk_name='id', **kwargs):
    now = datetime.datetime.now()
    pk_value = request.POST.get(pk_name)
    obj = model.objects.get(**{pk_name: pk_value}, **kwargs)
    for field in obj._meta.fields:
        if field.name in request.POST:
            setattr(obj, field.name, request.POST.get(field.name))
    obj.updat_date = now.strftime('%Y-%m-%d %H:%M:%S')
    obj.save()

    return JsonResponse({'result': 'success'})

def delete(request, model, pk_name='id', **kwargs):
    now = datetime.datetime.now()
    pk_value = request.POST.get(pk_name)

    obj = model.objects.get(**{pk_name: pk_value}, **kwargs)
    obj.use_yn = 'N'
    obj.updat_date = now.strftime('%Y-%m-%d %H:%M:%S')
    obj.save()

    return JsonResponse({'result': 'success'})
