from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..invoice.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView, CommonMainAddView
# Create your views here.

class invoiceIndex(CommonMainView):

   def custom_queryset(self):
      return  InvoiceMaster.objects.filter(use_yn='Y')


   def get(self, request, *args, **kwargs):
      self.title_nm = "INVOICE LIST"
      self.descript = "인보이스 페이지입니다"
      self.template_name = "invoice/index.html"
      self.target = "invoice"
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response 
   
   
class invoiceAdd(CommonMainAddView):
   def seletData(self):
      return { "master" : InvoiceMaster.objects.filter(id=self.id),
               "detail" : InvoiceDetail.objects.filter(invoice_id=self.id),
            }
   
   def selectOption(self, request):
      return {  }
   
   def get(self, request, *args, **kwargs):
      self.template_name = "invoice/add.html"
      self.pageType = request.GET.get('pageType', None)
      self.id = request.GET.get('id', None)
      self.type = request.GET.get('type', None)

      if self.pageType == 'I':
         self.title_nm = "인보이스추가"
         self.descript = "인보이스추가 페이지입니다"
      elif self.pageType == 'U':
         self.title_nm = "인보이스수정"
         self.descript = "인보이스수정 페이지입니다"

      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response


def invoiceSearch(request):
   return render(request, 'invoice/search.html')