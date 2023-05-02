from django.db import models
from ..common.common_models import commonModel, Tourconductor
from ..booking.models import BookingMaster


# Create your models here.
class RoomingMaster(commonModel):
    booking_id=models.ForeignKey(BookingMaster, db_column='BOOKING_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='수배 id')
    type=models.CharField(db_column='TYPE', max_length=2, verbose_name='TYPE')
    file_id=models.CharField(db_column='FILE_ID', max_length=20, verbose_name='매칭')
    total_pax=models.CharField(db_column='TOTAL_PAX', max_length=100, verbose_name='PAX')
    twin=models.CharField(db_column='TWIN', max_length=10, verbose_name='TWIN')
    triple=models.CharField(db_column='TRIPLE', max_length=10, verbose_name='TRIPLE')
    single=models.CharField(db_column='SINGLE', max_length=10, verbose_name='SINGLE')
    tc=models.ForeignKey(Tourconductor, db_column='tc', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='인솔자')
    tc_count=models.CharField(db_column='TC_COUNT', max_length=100, verbose_name='TC인원')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')

    class Meta:
        managed = False
        db_table = 'rooming_master'
        verbose_name = '루밍 마스터'
        verbose_name_plural = '루밍 마스터 목록'       


class RoomingDetail(commonModel):
    rooming_id=models.ForeignKey(RoomingMaster, db_column='ROOMING_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='루밍 id')
    room=models.CharField(db_column='ROOM', max_length=100, verbose_name='방')
    name_k=models.CharField(db_column='NAME_K', max_length=100, verbose_name='이름(한)')
    name_e=models.CharField(db_column='NAME_E', max_length=100, verbose_name='이름(영)')
    sex=models.CharField(db_column='SEX', max_length=2, verbose_name='성별')
    kubun=models.CharField(db_column='KUBUN', max_length=5, verbose_name='구분')
    birth=models.CharField(db_column='BIRTH', max_length=8, verbose_name='생년월일')
    passport=models.CharField(db_column='PASSPORT', max_length=9, verbose_name='여권')
    expirey=models.CharField(db_column='EXPIREY', max_length=8, verbose_name='말소일')
    mobile=models.CharField(db_column='MOBILE', max_length=13, verbose_name='연락처')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='기타')
 
  
    class Meta:
        managed = False
        db_table = 'rooming_detail'
        verbose_name = '루밍 디테일'
        verbose_name_plural = '루밍 디테일 목록'      