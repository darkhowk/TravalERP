from django.shortcuts import render
from django.views import generic
from .models import Menu
# Create your views here.

class invoiceIndex(generic.ListView):
   def __init__(self):
      self.title_nm = "인보이스"
      self.ogImgUrl = ""
      self.descript = "인보이스 페이지입니다"
      self.template_name = "invoice/index.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu
                     }

      return render(request, self.template_name, self.content)