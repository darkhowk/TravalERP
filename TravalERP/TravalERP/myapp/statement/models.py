from django.db import models
from ..common.common_models import commonModel, Agent, Manager
from ..invoice.models import InvoiceMaster

# Create your models here.
class StatementMaster(commonModel):
    invoice_id=models.ForeignKey(InvoiceMaster, db_column='INVOICE_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    type=models.CharField(db_column='TYPE', max_length=10, verbose_name='타입')
    agent=models.ForeignKey(Agent, db_column='AGENT', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='여행사', related_name='agents')
    manager=models.ForeignKey(Manager, db_column='MANAGER', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='매니저', related_name='managers')
    amt_type=models.CharField(db_column='AMT_TYPE', max_length=20, verbose_name='미과수')
    amt=models.CharField(db_column='AMT', max_length=20, verbose_name='금액')
    amt_unit=models.CharField(db_column='AMT_UNIT', max_length=20, verbose_name='단위')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')

    
    class Meta:
        managed = False
        db_table = 'statement_master'
        verbose_name = '정산서 마스터'
        verbose_name_plural = '정산서 마스터 목록'


class StatementDetail(commonModel):
    statement_id=models.ForeignKey(StatementMaster, db_column='STATEMENT_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    name=models.CharField(db_column='NAME', max_length=100, verbose_name='이름')
    amt=models.CharField(db_column='AMT', max_length=20, verbose_name='금액')
    people=models.CharField(db_column='PEOPLE', max_length=20, verbose_name='인원')
    remark=models.CharField(db_column='REMARK', max_length=2000, verbose_name='REMARK')

  
    class Meta:
        managed = False
        db_table = 'statement_detail'
        verbose_name = '정산서 디테일'
        verbose_name_plural = '정산서 디테일 목록'      
