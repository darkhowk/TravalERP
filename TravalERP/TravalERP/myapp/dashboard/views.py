from django.shortcuts import render
from django.views import generic
from ..common.common_models import Menu
# Create your views here.

class dashboardIndex(generic.ListView):
   def __init__(self):
      self.title_nm = "대시보드"
      self.ogImgUrl = ""
      self.descript = "대시보드 페이지입니다"
      self.template_name = "dashboard/index.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu
                     }

      return render(request, self.template_name, self.content)