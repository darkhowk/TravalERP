from django.db import models
from ..common.common_models import commonModel, Agent, Manager

# Create your models here.
class BookingMaster(commonModel):
    ref=models.CharField(db_column='REF', max_length=100, verbose_name='ref')  # Field name made lowercase.
    product_name=models.CharField(db_column='PRODUCT_NAME', max_length=100, verbose_name='상품명')  # Field name made lowercase.
    url=models.CharField(db_column='URL', max_length=100, verbose_name='url')  # Field name made lowercase.
    agent=models.ForeignKey(Agent, db_column='agent', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='여행사', related_name='booking_agents')
    manager=models.ForeignKey(Manager, db_column='manager', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='매니저', related_name='booking_managers')
    local_agent=models.ForeignKey(Agent, db_column='loc_agent', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='현지여행사', related_name='local_booking_agents')
    local_manager=models.ForeignKey(Manager, db_column='loc_manager', on_delete=models.SET_NULL, blank=True, null=True, verbose_name=' 현지매니저', related_name='local_booking_managers')
    kor_air_def=models.CharField(db_column='KOR_AIR_DEF', max_length=100, verbose_name='한국 출발일')  # Field name made lowercase.
    kor_air=models.CharField(db_column='KOR_AIR', max_length=100, verbose_name='한국 항공편')  # Field name made lowercase.
    kor_air_in=models.CharField(db_column='KOR_AIR_IN', max_length=100, verbose_name='한국 출발 공항')  # Field name made lowercase.
    kor_air_out=models.CharField(db_column='KOR_AIR_OUT', max_length=100, verbose_name='한국 도착 공항')  # Field name made lowercase.
    kor_air_time_dep=models.CharField(db_column='KOR_AIR_TIME_DEP', max_length=100, verbose_name='한국 출발시간')  # Field name made lowercase.
    kor_air_time_arri=models.CharField(db_column='KOR_AIR_TIME_ARRI', max_length=100, verbose_name='한국 도착시간')  # Field name made lowercase.
    loc_air_def=models.CharField(db_column='LOC_AIR_DEF', max_length=100, verbose_name='현지 출발일')  # Field name made lowercase.
    loc_air=models.CharField(db_column='LOC_AIR', max_length=100, verbose_name='현지 항공편')  # Field name made lowercase.
    loc_air_in=models.CharField(db_column='LOC_AIR_IN', max_length=100, verbose_name='현지 출발 공항')  # Field name made lowercase.
    loc_air_out=models.CharField(db_column='LOC_AIR_OUT', max_length=100, verbose_name='현지 도착 공항')  # Field name made lowercase.
    loc_air_time_dep=models.CharField(db_column='LOC_AIR_TIME_DEP', max_length=100, verbose_name='현지 출발시간')  # Field name made lowercase.
    loc_air_time_arri=models.CharField(db_column='LOC_AIR_TIME_ARRI', max_length=100, verbose_name='현지 도착시간')  # Field name made lowercase.
    breakfase=models.CharField(db_column='BREAKFAST', max_length=100, verbose_name='아침')  # Field name made lowercase.
    lunch=models.CharField(db_column='LUNCH', max_length=100, verbose_name='점심')  # Field name made lowercase.
    dinner=models.CharField(db_column='DINNER', max_length=100, verbose_name='저녁')  # Field name made lowercase.
    special=models.CharField(db_column='SPECIAL', max_length=1000, verbose_name='특식')  # Field name made lowercase.
    option=models.CharField(db_column='OPTION', max_length=1000, verbose_name='옵션')  # Field name made lowercase.
    shopping=models.CharField(db_column='SHOPPING', max_length=1000, verbose_name='쇼핑')  # Field name made lowercase.
    entrance=models.CharField(db_column='ENTRANCE', max_length=100, verbose_name='입장지')  # Field name made lowercase.
    bus=models.CharField(db_column='BUS', max_length=1000, verbose_name='버스')  # Field name made lowercase.
    kor_guide=models.CharField(db_column='KOR_GUIDE', max_length=1000, verbose_name='가이드')  # Field name made lowercase.
    loc_guide=models.CharField(db_column='LOC_GUIDE', max_length=1000, verbose_name='현지 가이드')  # Field name made lowercase.
    remark=models.CharField(db_column='REMARK', max_length=1000, verbose_name='REMARK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking_master'
        verbose_name = '수배내역'
        verbose_name_plural = '수배내역 목록'

class BookingDetail(commonModel):
    master_id=models.ForeignKey(BookingMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    type=models.CharField(db_column='TYPE', max_length=1, verbose_name='종류')  # Field name made lowercase.
    date=models.CharField(db_column='DATE', max_length=10, verbose_name='날짜')  # Field name made lowercase.
    schedule=models.CharField(db_column='SCHEDULE', max_length=100, verbose_name='일정')  # Field name made lowercase.
    loc=models.CharField(db_column='LOC', max_length=100, verbose_name='지역')  # Field name made lowercase.
    day=models.CharField(db_column='DAY', max_length=100, verbose_name='숙박일수')  # Field name made lowercase.
    hotel=models.CharField(db_column='HOTEL', max_length=100, verbose_name='호텔')  # Field name made lowercase.
    remark=models.CharField(db_column='REMARK', max_length=1000, verbose_name='REMARK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking_detail'
        verbose_name = '수배내역 상세 '
        verbose_name_plural = '수배내역 상세목록'

