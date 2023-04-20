from django.db import models
from ..common.common_models import commonModel, Tourconductor
from ..rooming.models import RoomingMaster

# Create your models here.
class ItineraryMaster(commonModel):
    master_id=models.ForeignKey(RoomingMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    tc=models.ForeignKey(Tourconductor, db_column='tc', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='인솔자')
    guide_loc=models.CharField(db_column='GUIDE_LOC', max_length=100, verbose_name='지역명')
    guide_name=models.CharField(db_column='GUIDE_NAME', max_length=20, verbose_name='이름')
    guide_tel=models.CharField(db_column='GUIDE_TEL', max_length=13, verbose_name='연락처')
    bus=models.CharField(db_column='BUS', max_length=1000, verbose_name='버스')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')
  
    class Meta:
        managed = False
        db_table = 'itinerary_master'
        verbose_name = '확정서 마스터'
        verbose_name_plural = '확정서 마스터 목록'     


class ItineraryHotel(commonModel):
    master_id=models.ForeignKey(ItineraryMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    hotel_star=models.CharField(db_column='HOTEL_STAR', max_length=10, verbose_name='성급')
    hotel_name=models.CharField(db_column='HOTEL_NAME', max_length=1200, verbose_name='호텔명')
    status=models.CharField(db_column='STATUS', max_length=10, verbose_name='상태')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')

    class Meta:
        managed = False
        db_table = 'itinerary_hotel'
        verbose_name = '확정서 호텔'
        verbose_name_plural = '확정서 호텔 목록'     


class ItinerarySchedule(commonModel):
    master_id=models.ForeignKey(ItineraryMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    date=models.CharField(db_column='DATE', max_length=20, verbose_name='날짜')
    air=models.CharField(db_column='AIR', max_length=20, verbose_name='항공')
    loc=models.CharField(db_column='LOC', max_length=200, verbose_name='지역')
 
    class Meta:
        managed = False
        db_table = 'itinerary_schedule'
        verbose_name = '확정서 스케쥴'
        verbose_name_plural = '확정서 스케쥴 목록'     
        

class ItineraryScheduleDetail(commonModel):
    master_id=models.ForeignKey(ItinerarySchedule, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    time=models.CharField(db_column='TIME', max_length=10, verbose_name='시간')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')
    loc_manager=models.CharField(db_column='LOC_MANAGER', max_length=20, verbose_name='로컬가이드')
 
    class Meta:
        managed = False
        db_table = 'itinerary_schedule_detail'
        verbose_name = '확정서 호텔 상세'
        verbose_name_plural = '확정서 호텔 상세 목록'    
