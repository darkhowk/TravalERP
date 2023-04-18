from django.db import models
from ..common.common_models import commonModel
from ..booking.models import BookingMaster

# Create your models here.
class RoomingMaster(commonModel):
    master_id=models.ForeignKey(BookingMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
  
    class Meta:
        managed = False
        db_table = 'rooming_master'
        verbose_name = '루밍 마스터'
        verbose_name_plural = '루밍 마스터 목록'       

class RoomingDetail(commonModel):
    master_id=models.ForeignKey(RoomingMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
 
  
    class Meta:
        managed = False
        db_table = 'rooming_detail'
        verbose_name = '루밍 디테일'
        verbose_name_plural = '루밍 디테일 목록'      