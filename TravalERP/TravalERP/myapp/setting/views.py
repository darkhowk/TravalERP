from django.shortcuts import render
from django.views import generic

from .models import Menu, Users
# Create your views here.

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