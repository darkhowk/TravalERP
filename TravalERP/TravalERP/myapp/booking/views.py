from django.shortcuts import render
from django.views import generic
# from ..common.common_models import Menu # 기존 Menu만 불러오던걸 주석
from ..common.common_models import * # 모든 모델 가져올수있게 변경
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
      optionData = {'agent': agent} # 추후 추가할 데이터를 위해
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "optionData" : optionData,
                     }

      return render(request, self.template_name, self.content)
   
class bookingAdd2(generic.ListView):
   def __init__(self):
      self.title_nm = "수배추가"
      self.ogImgUrl = ""
      self.descript = "수배추가 테스트페이지입니다"
      self.template_name = "booking/add2.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu
                     }

      return render(request, self.template_name, self.content)
   
class bookingAddModify(generic.ListView):
   def __init__(self):
      self.title_nm = "수배추가"
      self.ogImgUrl = ""
      self.descript = "수배추가 테스트페이지입니다"
      self.template_name = "booking/add_modify.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu
                     }

      return render(request, self.template_name, self.content)