from django.db import models
from ..common.common_models import commonModel
from ..itinerary.models import ItineraryMaster

# Create your models here.
class InvoiceMaster(commonModel):
    master_id=models.ForeignKey(ItineraryMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    invoice_type=models.CharField(db_column='INVOICE_TYPE', max_length=2, verbose_name='TYPE')
    total_pax=models.CharField(db_column='TOTAL_PAX', max_length=13, verbose_name='PAX')
    bank_id=models.CharField(db_column='BANK_ID', max_length=20, verbose_name='은행')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')

    
    class Meta:
        managed = False
        db_table = 'invoice_master'
        verbose_name = '인보이스 마스터'
        verbose_name_plural = '인보이스 마스터 목록'       

class InvoiceDetail(commonModel):
    master_id=models.ForeignKey(InvoiceMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    name=models.CharField(db_column='NAME', max_length=100, verbose_name='이름')
    amt=models.CharField(db_column='AMT', max_length=20, verbose_name='금액')
    people=models.CharField(db_column='PEOPLE', max_length=20, verbose_name='인원')
    day=models.CharField(db_column='DAY', max_length=20, verbose_name='박수')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')

  
    class Meta:
        managed = False
        db_table = 'invoice_detail'
        verbose_name = '인보이스 디테일'
        verbose_name_plural = '인보이스 디테일 목록'      





 