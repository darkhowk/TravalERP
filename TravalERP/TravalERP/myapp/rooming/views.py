from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from ..common.common_models import * # 기존 Menu만 불러오던걸 주석
from ..rooming.models import * # 모든 모델 가져올수있게 변경
import json
from ..common.CommonView import CommonMainView
# Create your views here.

class roomingIndex(CommonMainView):

   def custom_queryset(self):
      return  RoomingMaster, None, None

   def get(self, request, *args, **kwargs):
      self.title_nm = "ROOMING LIST"
      self.descript = "루밍리스트 페이지입니다"
      self.template_name = "rooming/index.html"
      self.target = "rooming"
      response = super().get(request, *args, **kwargs)
      
      if response is None:
         response = HttpResponse()
         
      return response 
   

class roomingAdd(generic.ListView):
   def __init__(self):
      self.title_nm = "루밍추가"
      self.ogImgUrl = ""
      self.descript = "루밍추가 페이지입니다"
      self.template_name = "rooming/add.html" 
      self.topMenu = Menu.objects.filter(menu_type="TOP")

   def get(self, request, *args, **kwargs):
      tourconductor = Tourconductor.objects.filter(use_yn ='Y')
      master = RoomingMaster.objects.filter(id=request.GET.get('id'))
      detail = RoomingDetail.objects.filter(master_id=request.GET.get('id'))
      selectData = {'master': master,'detail':detail}
      optionData = {'tourconductor': tourconductor}
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                        "topMenu"  : self.topMenu,
                        "optionData" : optionData,
                        "selectData" : selectData,
                     }

      return render(request, self.template_name, self.content)
   
def commonGetAjaxData(request, path, item):
   Models = pathtoMode(item)

   data = request.body.decode('utf-8')

   try:
      # JSON 형식으로 변환
      params = json.loads(data)
      data = list(Models.objects.filter(**params).values())
      return JsonResponse(data, safe=False)
      # JSON 형식이 맞는 경우 처리할 코드
   except json.decoder.JSONDecodeError:
        # JSON 형식이 아닌 경우 처리할 코드
      return JsonResponse(data, safe=False) 
   
def pathtoMode(path):
   if path == 'tourconductor':
      Models = Tourconductor
      
   return Models 