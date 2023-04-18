from django.db import models
from ..common.common_models import commonModel
from ..booking.models import BookingMaster

# Create your models here.
class InvoiceMaster(commonModel):
    
    class Meta:
        managed = False
        db_table = 'invoice_master'
        verbose_name = '인보이스 마스터'
        verbose_name_plural = '인보이스 마스터 목록'       

class InvoiceDetail(commonModel):
  
  
    class Meta:
        managed = False
        db_table = 'invoice_detail'
        verbose_name = '인보이스 디테일'
        verbose_name_plural = '인보이스 디테일 목록'      


