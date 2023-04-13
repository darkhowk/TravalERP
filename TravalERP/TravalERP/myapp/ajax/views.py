from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
# from ..common.common_models import Menu # 기존 Menu만 불러오던걸 주석
from ..common.common_models import * # 모든 모델 가져올수있게 변경
from ..booking.models import * # 모든 모델 가져올수있게 변경
import datetime, json
# Create your views here.

from django.db.models.functions import Concat
from django.db.models import F, Value, CharField

from django.db.models.functions import Now


def getData(request, item):
   Models = pathtoMode(item)

   data = request.body.decode('utf-8')
   
   try:
      # JSON 형식으로 변환
      params = json.loads(data)
      print(params)
      data = list(Models.objects.filter(**params).values())
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
    print(jsonData)
    print(fields)
    print("---------------")
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
   return Models
