from django.db import models
from ..common.common_models import commonModel
from ..rooming.models import RoomingMaster

# Create your models here.
class ItineraryMaster(commonModel):
    master_id=models.ForeignKey(RoomingMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
  
    class Meta:
        managed = False
        db_table = 'itinerary_master'
        verbose_name = '확정서 마스터'
        verbose_name_plural = '확정서 마스터 목록'       

class ItineraryHotel(commonModel):
    master_id=models.ForeignKey(ItineraryMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
 
  
    class Meta:
        managed = False
        db_table = 'itinerary_hotel'
        verbose_name = '확정서 호텔'
        verbose_name_plural = '확정서 호텔 목록'      

class ItinerarySchedule(commonModel):
    master_id=models.ForeignKey(ItineraryMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
 
  
    class Meta:
        managed = False
        db_table = 'itinerary_schedule'
        verbose_name = '확정서 스케쥴'
        verbose_name_plural = '확정서 스케쥴 목록'     

class ItineraryScheduleDetail(commonModel):
    master_id=models.ForeignKey(ItinerarySchedule, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
 
  
    class Meta:
        managed = False
        db_table = 'itinerary_schedule_detail'
        verbose_name = '확정서 호텔 상세'
        verbose_name_plural = '확정서 호텔 상세 목록'     
