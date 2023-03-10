from django.shortcuts import render
from django.views import generic
from ..common.common_models import Menu
# Create your views here.

class statementIndex(generic.ListView):
   def __init__(self):
        self.title_nm = "정산"
        self.ogImgUrl = ""
        self.descript = "정산 페이지입니다"
        self.template_name = "statement/index.html"
        self.topMenu = Menu.objects.filter(menu_type="TOP")

      
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                     }

      return render(request, self.template_name, self.content)