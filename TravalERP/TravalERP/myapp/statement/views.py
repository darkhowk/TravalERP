from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..statement.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView, CommonMainAddView
# Create your views here.

class statementIndex(CommonMainView):

   def custom_queryset(self):
      queryset = StatementMaster.objects.filter(use_yn='Y')
   
      if self.searchType != None and self.searchKeyword != None:
         return  queryset.filter( **{self.searchType+'__icontains': self.searchKeyword} )
      else:
         return queryset



   def get(self, request, *args, **kwargs):
      self.title_nm = "STATEMENT LIST"
      self.descript = "정산서 페이지입니다"
      self.template_name = "statement/index.html"
      self.target = "statement"
      self.searchType = request.GET.get('searchType', None)
      self.searchKeyword = request.GET.get('searchKeyword', None)
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response 
   

class statementAdd(CommonMainAddView):

   def seletData(self):
      return { "master" : StatementMaster.objects.filter(id=self.id),
               "detail" : StatementDetail.objects.filter(statement_id=self.id),
            }
   
   def selectOption(self, request):
      return {  

            }
   
   def get(self, request, *args, **kwargs): 
      self.template_name = "statement/add.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      self.type = request.GET.get('type', None)

      if self.pageType == 'I':
         self.title_nm = "정산서추가"
         self.descript = "정산서추가 페이지입니다"
      elif self.pageType == 'U':
         self.title_nm = "정산서수정"
         self.descript = "정산서수정 페이지입니다"

      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response