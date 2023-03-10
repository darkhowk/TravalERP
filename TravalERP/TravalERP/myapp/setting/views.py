import math
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.core.paginator import Paginator

import datetime

from ..common.common_models import Menu

# Create your views here.

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

class settingMenu(generic.ListView):
   def __init__(self):
      self.title_nm = "설정>메뉴관리"
      self.ogImgUrl = ""
      self.descript = "메뉴관리 페이지입니다"
      self.template_name = "setting/menu.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")
      self.leftMenu = Menu.objects.filter(menu_type="LEFT")

   def get(self, request, *args, **kwargs):
      ## 페이지에 뿌려질 데이터 
      # 페이지당 보여줄 개수
      self.per_page = int(request.GET.get('per_page', 5))

      # 현재 페이지
      self.current_page = int(request.GET.get('paging', 1))

      # 그려질 페이지 목록
      self.menus = Menu.objects.all()[self.per_page * (self.current_page - 1):self.per_page * self.current_page]

      # 페이지 수
      num_pages = math.ceil(Menu.objects.count() / self.per_page)

      # 페이지 번호 목록
      self.pages = range(1, num_pages + 1)

      ## 데이터들을 담는다
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "leftMenu"  : self.leftMenu,
                        "menus" : self.menus,
                        'pages': self.pages,
                        'current_page': int(self.current_page), 
                        'per_page': int(self.per_page),
                     }

      return render(request, self.template_name, self.content)
      

class settingAddMenu(generic.ListView):
   def __init__(self):
        self.title_nm = "설정>메뉴관리>메뉴추가"
        self.ogImgUrl = ""
        self.descript = "메뉴추가 페이지입니다"
        self.template_name = "setting/addMenu.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP")
        self.leftMenu = Menu.objects.filter(menu_type="LEFT")
      
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "leftMenu"  : self.leftMenu,
                     }

      return render(request, self.template_name, self.content)

def settingMenuInsert(request):
   now = datetime.datetime.now()

   menu = request.POST.get('menu')
   menu_name = request.POST.get('menu_name')
   upper_menu = request.POST.get('upper_menu')
   use_yn = request.POST.get('use_yn')
   icon = request.POST.get('icon')
   menu_type = request.POST.get('menu_type')
   link = request.POST.get('link')
   menu = Menu(
        menu=menu
      , menu_name=menu_name
      , upper_menu=upper_menu
      , use_yn=use_yn
      , icon=icon
      , menu_type=menu_type
      , link=link
      , entry_date = now.strftime('%Y-%m-%d %H:%M:%S')
   )
   menu.save()
   return JsonResponse({'result': 'success'})
