from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
# from ..common.common_models import Menu # 기존 Menu만 불러오던걸 주석
from ..common.common_models import * # 모든 모델 가져올수있게 변경
from ..booking.models import * # 모든 모델 가져올수있게 변경
from ..rooming.models import * # 모든 모델 가져올수있게 변경
from ..itinerary.models import * # 모든 모델 가져올수있게 변경
from ..invoice.models import * # 모든 모델 가져올수있게 변경
from ..statement.models import * # 모든 모델 가져올수있게 변경
import datetime, json
# Create your views here.

from django.db.models.functions import Concat
from django.db.models import F, Value, CharField

from django.db.models.functions import Now

import ftplib
from ftplib import FTP_TLS
import ssl
from django.http import HttpResponseBadRequest

def getData(request, item):
   Models = pathtoMode(item)

   data = request.body.decode('utf-8')
   
   try:
      # JSON 형식으로 변환
      params = json.loads(data)
      data = list(Models.objects.filter(**params).values())

      for row in data:
         for key, value in row.items():
            if value is None:
                  row[key] = ''
      return JsonResponse(data, safe=False)
      # JSON 형식이 맞는 경우 처리할 코드
   except json.decoder.JSONDecodeError:
        # JSON 형식이 아닌 경우 처리할 코드
      return JsonResponse(data, safe=False)
  

def getLikeData(request, item):
   Models = pathtoMode(item)

   data = request.body.decode('utf-8')
   
   try:
      # JSON 형식으로 변환
      params = json.loads(data)

      if params is None or not isinstance(params, dict):
          # params가 None이거나 딕셔너리가 아닌 경우 처리할 코드
          raise ValueError("params가 None이거나 딕셔너리가 아닙니다.")
      
      # params 딕셔너리 내의 값들을 수정하여 icontains 필터 적용
      filtered_params = {}
      for key, value in params.items():
         if key not in ['user_yn', 'master_id', 'id']:
            filtered_params[key + '__icontains'] = value
         else:
            filtered_params[key] = value
      data = list(Models.objects.filter(**filtered_params).values())
      return JsonResponse(data, safe=False)
      # JSON 형식이 맞는 경우 처리할 코드
   except json.decoder.JSONDecodeError:
        # JSON 형식이 아닌 경우 처리할 코드
      return JsonResponse(data, safe=False)

def dataInsert(request, item):
   # model별로 insert할 fields 작성
   fields = []
   Models = pathtoMode(item)
   
   fields = [f.name for f in Models._meta.fields if f.name not in ['entry_date', 'entry_id', 'updat_date', 'updat_id', 'id']]

   return insert(request, Models, fields)


def dataUpdate(request, item):
   Models = pathtoMode(item)
 
   type = request.POST.get('type', None)

   if type is None:
      return modify(request, Models)
   else: 
      return modify(request, Models, pk_name='id', type=type)

def dataDelete(request, item):
   Models = pathtoMode(item)

   type = request.POST.get('type', None)
   if type is None:
      return delete(request, Models)
   else: 
      return delete(request, Models, pk_name='id', type=type)

def masterInsert(request, item):
   # model별로 insert할 fields 작성
   fields = []
   Models = pathtoMode(item+'Master')
   fields = [f.name for f in Models._meta.fields if f.name not in ['entry_date', 'entry_id', 'updat_date', 'updat_id', 'id']]

   return insert(request, Models, fields)

def detailInsert(request, item):
   # model별로 insert할 fields 작성
   data = request.body
   data_list = json.loads(data.decode('utf-8'))
   fields = []
   Models = pathtoMode(item+'Detail')
   fields = [f.name for f in Models._meta.fields if f.name not in ['entry_date', 'entry_id', 'updat_date', 'updat_id', 'id']]
   for item in data_list:
      insertDetail(item, Models, fields)

   return JsonResponse({'result': 'success'})

def masterUpdate(request, item):
   Models = pathtoMode(item+'Master')
   type = request.POST.get('type', None)
   if type is None:
      return modify(request, Models)
   else: 
      return modify(request, Models, pk_name='id', type=type)

def detailupdate(request, item):
   data = request.body
   data_list = json.loads(data.decode('utf-8'))
   Models = pathtoMode(item+'Detail')
   type = request.POST.get('type', None)
   if type is None:
      for item in data_list:
         modifyDetail(item, Models)
   else: 
      for item in data_list:
         modifyDetail(item, Models, pk_name='id', type=type)
         
   return JsonResponse({'result': 'success'})

def masterDelete(request, item):
   Models = pathtoMode(item+'Master')
   type = request.POST.get('type', None)
   if type is None:
      return delete(request, Models)
   else: 
      return delete(request, Models, pk_name='id', type=type)

def detailDelete(request, item):

   data = request.body
   data_list = json.loads(data.decode('utf-8'))
   Models = pathtoMode(item+'Detail')
   type = request.POST.get('type', None)
   if type is None:
      for item in data_list:
         deleteDetail(item, Models)
   else: 
      for item in data_list:
         deleteDetail(item, Models, pk_name='id', type=type)
      
   return JsonResponse({'result': 'success'})

def dataCopy(request):
   target = request.POST.get('target', None)
   id = request.POST.get('id', None)
   now = datetime.datetime.now()
  
   if (target == 'schedule'):

      MasterModels = pathtoMode(target+'Master')
      MasterQueryset = MasterModels.objects.filter(id=id).select_related('agent').select_related('manager')

      newMasterQueryset = MasterQueryset.annotate(
           new_product_name=Concat('product_name', Value('_copy'))
         , new_entry_date=Now()
         , new_use_yn =Value('N')
      ).values(
           'new_product_name'
         , 'new_entry_date'
         , 'new_use_yn'
         , 'entry_id'
         , 'location'
         , 'start'
         , 'night'
         , 'day'
         , 'bus'
         , 'entrance'
         , 'breakfast'
         , 'lunch'
         , 'dinner'
         , 'special'
         , 'option'
         , 'shopping'
         , 'schedule_remark'
         , 'agent'
         , 'manager'
      )

      # 이전의 id 필드는 제외합니다.
      new_queryset = newMasterQueryset.exclude(id__isnull=False, updat_date__isnull=False, updat_id__isnull=False)

      # 변경한 쿼리셋을 DB에 저장합니다.
      new_master_instances = []
      for row in new_queryset:
         agent_id = row['agent']
         agent = Agent.objects.get(id=agent_id)
         row['agent'] = agent
         manager_id = row['manager']
         manager = Manager.objects.get(id=manager_id)
         row['manager'] = manager
         new_master_instance = MasterModels.objects.create(
            product_name=row['new_product_name'],
            entry_date=row['new_entry_date'],
            use_yn=row['new_use_yn'],
            location=row['location'],
            start=row['start'],
            night=row['night'],
            day=row['day'],
            bus=row['bus'],
            entrance=row['entrance'],
            breakfast=row['breakfast'],
            lunch=row['lunch'],
            dinner=row['dinner'],
            special=row['special'],
            option=row['option'],
            shopping=row['shopping'],
            schedule_remark=row['schedule_remark'],
            agent=agent,
            manager=manager,
         )
         new_master_instances.append(new_master_instance)

      new_master_id =  new_master_instance.id
            
      DeatilModels = pathtoMode(target+'Detail')
      DeatilQueryset = DeatilModels.objects.filter(master_id=id)

      newDetailQueryset = DeatilQueryset.annotate(
         new_entry_date=Now(),
         new_use_yn=Value('N'),
      ).values(
         'new_entry_date',
         'new_use_yn',
         'master_id',
         'entry_id',
         'day',
         'schedule',
         'hotel',
      )

      # 이전의 id 필드는 제외합니다.
      new_queryset = newDetailQueryset.exclude(id__isnull=False, updat_date__isnull=False, updat_id__isnull=False)
      master_instance = ScheduleMaster.objects.get(id=new_master_id)
      # 변경한 쿼리셋을 DB에 저장합니다.
      new_detail_instances = []
      for row in new_queryset:
         row['master_id'] = master_instance
         new_detail_instance = DeatilModels.objects.create(
            entry_date=row['new_entry_date'],
            use_yn=row['new_use_yn'],
            day=row['day'],
            schedule=row['schedule'],
            hotel=row['hotel'],
            master_id= row['master_id'],
         )
         new_detail_instances.append(new_detail_instance)

      return JsonResponse({'result': 'success'})


#################################################
# 기본 구문
#################################################

def insert(request, model, fields):
    now = datetime.datetime.now()
    data = {}
    for field in fields:
      field_instance = model._meta.get_field(field)
      if isinstance(field_instance, models.ForeignKey):
         # ForeignKey field 처리
         print("??")
         print(request.POST.get(field))
         print(field)
         data[field] = pathtoMode(field).objects.get(id=request.POST.get(field))
      else:
         # 일반 field 처리
         data[field] = request.POST.get(field)

    obj = model(**data, entry_date=now.strftime('%Y-%m-%d %H:%M:%S'))
    obj.save()

    return JsonResponse({'result': 'success', 'id': obj.id})

def modify(request, model, pk_name='id', **kwargs):
    now = datetime.datetime.now()
    pk_value = request.POST.get(pk_name)
    obj = model.objects.get(**{pk_name: pk_value}, **kwargs)
    for field in obj._meta.fields:
        if field.name in request.POST:
            # Check if field is a foreign key
            if isinstance(field, models.ForeignKey):
               fk_id = request.POST.get(field.name)
               # Get the related model instance using the foreign key id
               related_model = field.related_model.objects.get(id=fk_id)
               setattr(obj, field.name, related_model)
            else:
               setattr(obj, field.name, request.POST.get(field.name))
    obj.updat_date = now.strftime('%Y-%m-%d %H:%M:%S')
    obj.save()

    return JsonResponse({'result': 'success', 'id': obj.id})

def delete(request, model, pk_name='id', **kwargs):
    now = datetime.datetime.now()
    pk_value = request.POST.get(pk_name)

    obj = model.objects.get(**{pk_name: pk_value}, **kwargs)
    obj.use_yn = 'N'
    obj.updat_date = now.strftime('%Y-%m-%d %H:%M:%S')
    obj.save()

    return JsonResponse({'result': 'success', 'id': obj.id})

def insertDetail(jsonData, model, fields):
    now = datetime.datetime.now()
    data = {}
    for field in fields:
      if field in jsonData:
         field_instance = model._meta.get_field(field)
         if isinstance(field_instance, models.ForeignKey):
            # ForeignKey field 처리
            if model == ScheduleDetail:
               if field == 'master_id':
                  data[field] = ScheduleMaster.objects.get(id=jsonData[field])
               else:
                  data[field] = pathtoMode(field).objects.get(id=jsonData[field])
            elif model == BookingDetail:
               if field == 'master_id':
                  data[field] = BookingMaster.objects.get(id=jsonData[field])
               else:
                  data[field] = pathtoMode(field).objects.get(id=jsonData[field])
         else:
            # 일반 field 처리
            data[field] = jsonData[field]
      else:
         data[field] = None  

    obj = model(**data, entry_date=now.strftime('%Y-%m-%d %H:%M:%S'))
    obj.save()

    return JsonResponse({'result': 'success', 'id': obj.id})

def modifyDetail(jsonData, model, pk_name='id', **kwargs):
    now = datetime.datetime.now()
    pk_value = jsonData[pk_name]
    obj = model.objects.get(**{pk_name: pk_value}, **kwargs)
    for field in obj._meta.fields:
        if field.name in jsonData:
            # Check if field is a foreign key
            if isinstance(field, models.ForeignKey):
               fk_id = jsonData.get(field.name)
               # Get the related model instance using the foreign key id
               related_model = field.related_model.objects.get(id=fk_id)
               setattr(obj, field.name, related_model)
            else:
               setattr(obj, field.name, jsonData.get(field.name))
    obj.updat_date = now.strftime('%Y-%m-%d %H:%M:%S')
    obj.save()

    return JsonResponse({'result': 'success', 'id': obj.id})

def deleteDetail(jsonData, model, pk_name='id', **kwargs):
   now = datetime.datetime.now()
   pk_value = jsonData[pk_name]

   obj = model.objects.get(**{pk_name: pk_value}, **kwargs)
   for field in obj._meta.fields:
      if field.name in jsonData:
         # Check if field is a foreign key
         if isinstance(field, models.ForeignKey):
            fk_id = jsonData.get(field.name)
            # Get the related model instance using the foreign key id
            related_model = field.related_model.objects.get(id=fk_id)
            setattr(obj, field.name, related_model)
         else:
            setattr(obj, field.name, jsonData.get(field.name))
   obj.use_yn = 'N'
   obj.updat_date = now.strftime('%Y-%m-%d %H:%M:%S')
   obj.save()

   return JsonResponse({'result': 'success', 'id': obj.id})

def pathtoMode(path):
   if path == 'local_agent':
      Models = Agent
   if path == 'local_manager':
      Models = Manager
   if path == 'agent':
      Models = Agent
   if path == 'attn_agent':
      Models = Agent
   if path == 'attn_manager':
      Models = Manager
   if path == 'from_agent':
      Models = Agent
   if path == 'from_manager':
      Models = Manager
   if path == 'airport':
      Models = Airport
   if path == 'bank':
      Models = Bank
   if path == 'commcode':
      Models = CommCode
   if path == 'hotel':
      Models = Hotel
   if path == 'manager':
      Models = Manager
   if path == 'menu':
      Models = Menu
   if path == 'scheduleMaster':
      Models = ScheduleMaster
   if path == 'scheduleDetail':
      Models = ScheduleDetail
   if path == 'bookingMaster':
      Models = BookingMaster
   if path == 'bookingDetail':
      Models = BookingDetail
   if path == 'citycode':
      Models = Citycode
   if path == 'tourconductor':
      Models = Tourconductor
   if path == 'roomingMaster':
      Models = RoomingMaster
   if path == 'roomingDetail':
      Models = RoomingDetail
   return Models


def file_upload(request, item):
   if request.method == 'POST':
      # Get the file from the request
      file = request.FILES.get('file')
      if not file:
         return HttpResponseBadRequest('No file uploaded')

      # Connect to the FTPS server
      ftps = FTP_TLS(host='tontour.myds.me', user='landcrs', passwd='xldhdpsxndj1234')
      ftps.prot_p()
      ftps.cwd('/LANDCRS_UPLOAD')

      # Upload the file
      try:
         ftps.storbinary('STOR %s' % file.name, file)
      except ftplib.all_errors as e:
         return HttpResponseBadRequest('Failed to upload file: %s' % str(e))
      finally:
         ftps.quit()

      return HttpResponse('File uploaded successfully')
   else:
      return render(request, 'upload_form.html')
   
import sys
import pandas as pd
sys.path.append(pd.__path__[0])

from openpyxl import load_workbook

def excelUpload(request, item):
   if request.method == 'POST':
      file = request.FILES['file']
      wb = load_workbook(filename=file, read_only=False)
      ws = wb.active

      # Do something with the worksheet
      # ...

      # Convert the worksheet to HTML table
      table = "<table>"
      merged_cells = ws.merged_cells.ranges
      for row in ws.rows:
         table += "<tr>"
         for cell in row:
               value = cell.value
               rowspan, colspan = 1, 1
               for merged_range in merged_cells:
                  if cell.coordinate in merged_range:
                     top_left_cell = merged_range.start_cell
                     rowspan = merged_range.size['rows']
                     colspan = merged_range.size['columns']
                     if cell.coordinate != top_left_cell.coordinate:
                           value = None
                     break
               if value is None:
                  continue
               attrs = ""
               if rowspan > 1:
                  attrs += f" rowspan='{rowspan}'"
               if colspan > 1:
                  attrs += f" colspan='{colspan}'"
               table += f"<td{attrs}>{value}</td>"
         table += "</tr>"
      table += "</table>"

      return HttpResponse(table)

   return render(request, 'upload_form.html')


def getREF(request, target):
   # target 에 따라서 리턴할 id값이 달라짐
   data = request.body.decode('utf-8')

      # JSON 형식으로 변환
   params = json.loads(data)
   ref = params.get("ref")
   use_yn = params.get("use_yn")
   # ref 검색 booking ref
   refObj = BookingMaster.objects.filter(ref__icontains=ref, use_yn=use_yn)
   id_list = [obj.id for obj in refObj]
   print(target)
   if target in ['itinerary', 'invoice', 'statement'] : # 확정서
      # 루밍에서 해당 ref로 루밍 id검색하여 master_id로 리턴
      tmpObj = RoomingMaster.objects.filter(booking_id__in=id_list);
      id_list = [obj.id for obj in tmpObj]
   if target in ['invoice','statement']: # 인보이스
      tmpObj = InvoiceMaster.objects.filter(itinerary_id__in=id_list);
      id_list = [obj.id for obj in tmpObj]
   if target == 'statement': # 정산
      tmpObj = StatementMaster.objects.filter(invoice_id__in=id_list);
      id_list = [obj.id for obj in tmpObj]

   refObj = list(BookingMaster.objects.filter(ref__icontains=ref, use_yn=use_yn).values())

   # 해당 id를 master_id로 변경하여 리턴
   if len(id_list) > 0:
      resultData = {
         'refList' : refObj,
         'master_id': id_list,
         'result' : 1
      }
   else:
      resultData = {
         'result' : 0
      }

   return JsonResponse(resultData, safe=False)
