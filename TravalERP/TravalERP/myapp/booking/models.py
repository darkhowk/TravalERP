from django.db import models
from ..common.common_models import commonModel, Agent, Manager

# Create your models here.
class BookingMaster(commonModel):
    yyyy=models.CharField(db_column='YYYY', max_length=4, verbose_name='년도')  # Field name made lowercase.y
    ref=models.CharField(db_column='REF', max_length=20, verbose_name='레퍼런스')  # Field name made lowercase.
    attn_agent=models.ForeignKey(Agent, db_column='attn_agent', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='여행사', related_name='attn_agents')
    attn_manager=models.ForeignKey(Manager, db_column='attn_manager', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='여행사 담당자', related_name='attn_managers')
    from_agent=models.ForeignKey(Agent, db_column='from_agent', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='현지 여행사', related_name='from_agents')
    from_manager=models.ForeignKey(Manager, db_column='from_manager', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='현지 담당자', related_name='from_managers')
    product_name=models.CharField(db_column='PRODUCT_NAME', max_length=100, verbose_name='상품명')  # Field name made lowercase.
    kor_air_date=models.CharField(db_column='KOR_AIR_DATE', max_length=100, verbose_name='한국 출발일')  # Field name made lowercase.
    kor_air_in=models.CharField(db_column='KOR_AIR_IN', max_length=100, verbose_name='한국 출발공항')  # Field name made lowercase.
    kor_air_out=models.CharField(db_column='KOR_AIR_OUT', max_length=100, verbose_name='현지 도착공항')  # Field name made lowercase.
    kor_air=models.CharField(db_column='KOR_AIR', max_length=100, verbose_name='한국 항공편')  # Field name made lowercase.
    kor_air_dep_time=models.CharField(db_column='KOR_AIR_DEP_TIME', max_length=100, verbose_name='한국 출발시간')  # Field name made lowercase.
    kor_air_ari_time=models.CharField(db_column='KOR_AIR_ARI_TIME', max_length=100, verbose_name='현지 도착시간')  # Field name made lowercase.
    loc_air_date=models.CharField(db_column='LOC_AIR_DATE', max_length=100, verbose_name='현지 출발일')  # Field name made lowercase.
    loc_air_in=models.CharField(db_column='LOC_AIR_IN', max_length=100, verbose_name='현지 출발공항')  # Field name made lowercase.
    loc_air_out=models.CharField(db_column='LOC_AIR_OUT', max_length=100, verbose_name='한국 도착공항')  # Field name made lowercase.
    loc_air=models.CharField(db_column='LOC_AIR', max_length=100, verbose_name='현지 항공편')  # Field name made lowercase.
    loc_air_dep_time=models.CharField(db_column='LOC_AIR_DEP_TIME', max_length=100, verbose_name='현지 출발시간')  # Field name made lowercase.
    loc_air_ari_time=models.CharField(db_column='LOC_AIR_ARI_TIME', max_length=100, verbose_name='한국 도착시간')  # Field name made lowercase.
    pax=models.CharField(db_column='PAX', max_length=100, verbose_name='인원')  # Field name made lowercase.
    bus=models.CharField(db_column='BUS', max_length=1000, verbose_name='버스')  # Field name made lowercase.
    entrance=models.CharField(db_column='ENTRANCE', max_length=100, verbose_name='입장지')  # Field name made lowercase.
    breakfast=models.CharField(db_column='BREAKFAST', max_length=100, verbose_name='아침')  # Field name made lowercase.
    lunch=models.CharField(db_column='LUNCH', max_length=100, verbose_name='점심')  # Field name made lowercase.
    dinner=models.CharField(db_column='DINNER', max_length=100, verbose_name='저녁')  # Field name made lowercase.
    special=models.CharField(db_column='SPECIAL', max_length=1000, verbose_name='특식')  # Field name made lowercase.
    option=models.CharField(db_column='OPTION', max_length=1000, verbose_name='옵션 여행지')  # Field name made lowercase.
    guide_kor=models.CharField(db_column='GUIDE_KOR', max_length=1000, verbose_name='한국인 가이드')  # Field name made lowercase.
    guide_loc=models.CharField(db_column='GUIDE_LOC', max_length=1000, verbose_name='현지 가이드')  # Field name made lowercase.
    url=models.CharField(db_column='URL', max_length=100, verbose_name='주소')  # Field name made lowercase.
    remark=models.CharField(db_column='REMARK', max_length=1000, verbose_name='기타')  # Field name made lowercase. 
    include=models.CharField(db_column='INCLUDE', max_length=1000, verbose_name='포함')  # Field name made lowercase.
    not_include=models.CharField(db_column='NOT_INCLUDE', max_length=1000, verbose_name='불포함')  # Field name made lowercase.
    hotel=models.CharField(db_column='HOTEL', max_length=1000, verbose_name='호텔')  # Field name made lowercase.
    product_manager = models.CharField(db_column='PRODUCT_MANAGER', max_length=200, verbose_name='상품 담당자')

    class Meta:
        managed = False
        db_table = 'booking_master'
        verbose_name = '수배내역'
        verbose_name_plural = '수배내역 목록'

class BookingDetail(commonModel):
    booking_id=models.ForeignKey(BookingMaster, db_column='BOOKING_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 id')
    date=models.CharField(db_column='DATE', max_length=10, verbose_name='날짜')  # Field name made lowercase.
    schedule=models.CharField(db_column='SCHEDULE', max_length=100, verbose_name='일정')  # Field name made lowercase.
    loc=models.CharField(db_column='LOC', max_length=100, verbose_name='지역')  # Field name made lowercase.
    day=models.CharField(db_column='DAY', max_length=100, verbose_name='숙박일수')  # Field name made lowercase.
    hotel=models.CharField(db_column='HOTEL', max_length=100, verbose_name='호텔')  # Field name made lowercase.
    remark=models.CharField(db_column='REMARK', max_length=1000, verbose_name='REMARK')  # Field name made lowercase.
    type=models.CharField(db_column='TYPE', max_length=1, verbose_name='종류')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking_detail'
        verbose_name = '수배내역 상세 '
        verbose_name_plural = '수배내역 상세목록'

