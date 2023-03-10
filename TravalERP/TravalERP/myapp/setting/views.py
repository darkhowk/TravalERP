from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
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
        self.Menu = Menu.objects.all()
      
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "leftMenu"  : self.leftMenu,
                        "Menu" : self.Menu
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
