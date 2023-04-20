from django.db import models
from ..common.common_models import commonModel
from ..booking.models import BookingMaster

# Create your models here.
class RoomingMaster(commonModel):
    master_id=models.ForeignKey(BookingMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    type=models.CharField(db_column='TYPE', max_length=2, verbose_name='TYPE')
    file_id=models.CharField(db_column='FILE_ID', max_length=20, verbose_name='매칭')
    total_pax=models.CharField(db_column='TOTAL_PAX', max_length=100, verbose_name='PAX')
    twin=models.CharField(db_column='TWIN', max_length=10, verbose_name='TWIN')
    triple=models.CharField(db_column='TRIPLE', max_length=10, verbose_name='TRIPLE')
    single=models.CharField(db_column='SINGLE', max_length=10, verbose_name='SINGLE')
    tc=models.CharField(db_column='TC', max_length=20, verbose_name='TOUR LEADER')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')

    class Meta:
        managed = False
        db_table = 'rooming_master'
        verbose_name = '루밍 마스터'
        verbose_name_plural = '루밍 마스터 목록'       


class RoomingDetail(commonModel):
    master_id=models.ForeignKey(RoomingMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    room_type=models.CharField(db_column='ROOM_TYPE', max_length=100, verbose_name='ROOM')
    name_ko=models.CharField(db_column='NAME_KO', max_length=100, verbose_name='NAME(K)')
    name_en=models.CharField(db_column='NAME_EN', max_length=100, verbose_name='NAME(E)')
    sex=models.CharField(db_column='SEX', max_length=2, verbose_name='SEX')
    kubun=models.CharField(db_column='KUBUN', max_length=5, verbose_name='구분')
    birth=models.CharField(db_column='BIRTH', max_length=8, verbose_name='DATE OF BIRTH')
    passport=models.CharField(db_column='PASSPORT', max_length=9, verbose_name='PASSPORT')
    expiry=models.CharField(db_column='EXPIRY', max_length=8, verbose_name='DATE OF EXPIRY')
    mobile=models.CharField(db_column='MOBILE', max_length=13, verbose_name='MOBILE')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')
 
  
    class Meta:
        managed = False
        db_table = 'rooming_detail'
        verbose_name = '루밍 디테일'
        verbose_name_plural = '루밍 디테일 목록'      