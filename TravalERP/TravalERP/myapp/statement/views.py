from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..statement.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView
# Create your views here.

class statementIndex(CommonMainView):

   def custom_queryset(self):
      return  StatementMaster, None, None


   def get(self, request, *args, **kwargs):
      self.title_nm = "STATEMENT LIST"
      self.descript = "정산서 페이지입니다"
      self.template_name = "statement/index.html"
      self.target = "statement"
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response 
   
class statementAdd(generic.ListView):
   def __init__(self):
      self.title_nm = "정산추가"
      self.ogImgUrl = ""
      self.descript = "정산추가 페이지입니다"
      self.template_name = "statement/add.html"
      self.topMenu = Menu.objects.filter(menu_type="TOP") 

   def get(self, request, *args, **kwargs):
      agent = Agent.objects.filter(use_yn ='Y', type='A')
      manager = Manager.objects.filter(use_yn ='Y', type='M')
      master = StatementMaster.objects.filter(id=request.GET.get('id'))
      detail = StatementDetail.objects.filter(master_id=request.GET.get('id'))
      optionData = {'agent': agent, 'manager' : manager} 
      selectData = {'master': master,'detail':detail}
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "optionData" : optionData,
                        "selectData" : selectData,
                     } 

      return render(request, self.template_name, self.content) 


def pathtoMode(path):
   if path == 'agent':
      Models = Agent
   if path == 'manager':
      Models = Manager
   return Models
