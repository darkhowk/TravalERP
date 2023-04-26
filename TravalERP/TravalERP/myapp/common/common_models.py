from django.db import models

class commonModel(models.Model):
    use_yn = models.CharField(db_column='USE_YN', max_length=100, verbose_name='사용여부')  # Field name made lowercase.
    entry_id = models.CharField(db_column='ENTRY_ID', max_length=20, verbose_name='등록자')  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE', verbose_name='등록일')  # Field name made lowercase.
    updat_id = models.CharField(db_column='UPDAT_ID', max_length=20, blank=True, null=True, verbose_name='수정자')  # Field name made lowercase.
    updat_date = models.DateTimeField(db_column='UPDAT_DATE', blank=True, null=True, verbose_name='수정일')  # Field name made lowercase.
    
    class Meta:
        abstract = True

class Menu(commonModel):
    menu = models.CharField(db_column='MENU', max_length=10, verbose_name='메뉴')  # Field name made lowercase.
    menu_name = models.CharField(db_column='MENU_NAME', max_length=100, verbose_name='메뉴명')  # Field name made lowercase.
    upper_menu = models.CharField(db_column='UPPER_MENU', max_length=10, blank=True, null=True, verbose_name='상위메뉴')  # Field name made lowercase.
    icon = models.CharField(db_column='ICON', max_length=100, blank=True, null=True, verbose_name='아이콘')  # Field name made lowercase.
    menu_type = models.CharField(db_column='MENU_TYPE', max_length=10, verbose_name='메뉴타입')  # Field name made lowercase.
    link = models.CharField(db_column='LINK', max_length=1000, verbose_name='링크')
    
    def __iter__(self):
        yield self.menu
        yield self.menu_name
        yield self.upper_menu
        yield self.icon
        yield self.menu_type
        yield self.link
    
    class Meta:
        managed = False
        db_table = 'menu'
        verbose_name = '메뉴'
        verbose_name_plural = '메뉴 목록'

class Agent(commonModel):
    agent_name= models.CharField(db_column='AGENT_NAME', max_length=100, verbose_name='여행사')  # Field name made lowercase.
    agent_tel= models.CharField(db_column='AGENT_TEL', max_length=100, verbose_name='대표전화')  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=100, verbose_name='TYPE')  # Field name made lowercase.

    def __iter__(self):
        yield self.agent_name
        yield self.agent_tel

    class Meta:
        managed = False
        db_table = 'agent'
        verbose_name = '여행사'
        verbose_name_plural = '여행사 목록' 

class Manager(commonModel):
    agent= models.ForeignKey(Agent, db_column='agent', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='여행사')
    manager_name= models.CharField(db_column='MANAGER_NAME', max_length=100, verbose_name='담당자명')  # Field name made lowercase.
    manager_tel= models.CharField(db_column='MANAGER_TEL', max_length=20, verbose_name='담당자 연락처')  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=100, verbose_name='TYPE')  # Field name made lowercase.
    manager_hp = models.CharField(db_column='MANAGER_HP', max_length=100, verbose_name='담당자 휴대폰')  # Field name made lowercase.
    manager_messenger = models.CharField(db_column='MANAGER_MESSENGER', max_length=100, verbose_name='담당자 메신저')  # Field name made lowercase.
    manager_email = models.CharField(db_column='MANAGER_EMAIL', max_length=100, verbose_name='담당자 이메일')  # Field name made lowercase.
    manager_remark = models.TextField(db_column='MANAGER_REMARK', max_length=1000, blank=True, null=True, verbose_name='REMARK')  # Field name made lowercase.

    def __str__(self):
        return f"{self.agent} - {self.agent.agent_name}"
    
    def __iter__(self):
        yield self.agent.agent_name
        yield self.manager_name
        yield self.manager_tel
        yield self.manager_hp
        yield self.manager_messenger
        yield self.manager_email
        yield self.manager_remark
        
    class Meta:
        managed = False
        db_table = 'manager'
        verbose_name = '담당자'
        verbose_name_plural = '담당자 목록'

class Airport(commonModel):
    airport_name= models.CharField(db_column='AIRPORT_NAME', max_length=100, verbose_name='편명')
    departure_airport= models.CharField(db_column='DEPARTURE_AIRPORT', max_length=100, verbose_name='출발공항')
    departure_city = models.CharField(db_column='DEPARTURE_CITY', max_length=100, verbose_name='출발도시')
    departure_time = models.CharField(db_column='DEPARTURE_TIME', max_length=100, verbose_name='출발시간')
    arrival_airport= models.CharField(db_column='ARRIVAL_AIRPORT', max_length=100, verbose_name='도착공항')
    arrival_city = models.CharField(db_column='ARRIVAL_CITY', max_length=100, verbose_name='도착도시')
    arrival_time = models.CharField(db_column='ARRIVAL_TIME', max_length=100, verbose_name='도착시간')
    time_taken = models.TextField(db_column='TIME_TAKEN', max_length=1000, verbose_name='소요시간')
    airport_remark = models.TextField(db_column='AIRPORT_REMARK', max_length=1000, blank=True, null=True, verbose_name='REMARK')
    
    def __iter__(self):
        yield self.airport_name
        yield self.departure_airport
        yield self.departure_city
        yield self.departure_time
        yield self.arrival_airport
        yield self.arrival_city
        yield self.arrival_time
        yield self.time_taken
        yield self.airport_remark

    class Meta:
        managed = False
        db_table = 'airport'
        verbose_name = '항공'
        verbose_name_plural = '항공 목록'

class CommCode(commonModel):
    code = models.CharField(db_column='CODE', max_length=100, verbose_name='코드')
    code_name = models.CharField(db_column='CODE_NAME', max_length=100, verbose_name='코드명')
    code_etc1 = models.CharField(db_column='CODE_ETC1', max_length=100, verbose_name='기타1')
    code_etc2 = models.CharField(db_column='CODE_ETC2', max_length=100, verbose_name='기타2')
    code_etc3 = models.CharField(db_column='CODE_ETC3', max_length=100, verbose_name='기타3')
    code_etc4 = models.CharField(db_column='CODE_ETC4', max_length=100, verbose_name='기타4')
    code_etc5 = models.CharField(db_column='CODE_ETC5', max_length=100, verbose_name='기타5')
    
    def __iter__(self):
        yield self.code
        yield self.code_name
        yield self.code_etc1
        yield self.code_etc2
        yield self.code_etc3
        yield self.code_etc4
        yield self.code_etc5

    class Meta:
        managed = False
        db_table = 'commcode'
        verbose_name = '공통코드'
        verbose_name_plural = '공통코드 목록'

class Bank(commonModel):
    bank_name = models.CharField(db_column='BANK_NAME', max_length=100, verbose_name='은행명')
    account_name = models.CharField(db_column='ACCOUNT_NAME', max_length=100, verbose_name='예금주')
    account_no = models.CharField(db_column='ACCOUNT_NO', max_length=100, verbose_name='계좌번호')
    swift = models.CharField(db_column='SWIFT', max_length=100, verbose_name='SWIFT')
    iban_code = models.CharField(db_column='IBAN_CODE', max_length=100, verbose_name='IBAN_CODE')
    branch = models.CharField(db_column='BRANCH', max_length=100, verbose_name='BRANCH')
    haa = models.CharField(db_column='HAA', max_length=100, verbose_name='국내/국외')
    bank_remark = models.TextField(db_column='BANK_REMARK', max_length=1000, verbose_name='REMARK')
    
    def __iter__(self):
        yield self.bank_name
        yield self.account_name
        yield self.account_no
        yield self.swift
        yield self.iban_code
        yield self.branch
        yield self.haa
        yield self.bank_remark

    class Meta:
        managed = False
        db_table = 'bank'
        verbose_name = '은행'
        verbose_name_plural = '은행 목록'

class Hotel(commonModel):
    hotel_name = models.CharField(db_column='HOTEL_NAME', max_length=100, verbose_name='호텔명')
    hotel_en_name = models.CharField(db_column='HOTEL_EN_NAME', max_length=100, verbose_name='호텔명(영어)')
    rank = models.CharField(db_column='RANK', max_length=100, verbose_name='등급')
    country = models.CharField(db_column='COUNTRY', max_length=100, verbose_name='국가')
    city = models.CharField(db_column='CITY', max_length=100, verbose_name='도시')
    address = models.CharField(db_column='ADDRESS', max_length=1000, verbose_name='주소')
    hotel_tel = models.CharField(db_column='HOTEL_TEL', max_length=100, verbose_name='연락처')
    hotel_remark = models.TextField(db_column='HOTEL_REMARK', max_length=1000, verbose_name='REMARK')
    url = models.TextField(db_column='URL', max_length=1000, verbose_name='웹사이트')
    
    def __iter__(self):
        yield self.hotel_name
        yield self.hotel_en_name
        yield self.rank
        yield self.country
        yield self.city
        yield self.hotel_tel
        yield self.hotel_remark

    class Meta:
        managed = False
        db_table = 'hotel'
        verbose_name = '호텔'
        verbose_name_plural = '호텔 목록'

class Traval(commonModel):
    traval_name = models.CharField(db_column='HOTEL_NAME', max_length=100, verbose_name='호텔명')
    traval_en_name = models.CharField(db_column='HOTEL_EN_NAME', max_length=100, verbose_name='호텔명(영어)')
    rank = models.CharField(db_column='RANK', max_length=100, verbose_name='등급')
    country = models.CharField(db_column='COUNTRY', max_length=100, verbose_name='국가')
    city = models.CharField(db_column='CITY', max_length=100, verbose_name='도시')
    address = models.CharField(db_column='ADDRESS', max_length=1000, verbose_name='주소')
    hotel_tel = models.CharField(db_column='HOTEL_TEL', max_length=100, verbose_name='전화번호')
    hotel_remark = models.TextField(db_column='HOTEL_REMARK', max_length=1000, verbose_name='REMARK')
    
    def __iter__(self):
        yield self.hotel_name
        yield self.hotel_en_name
        yield self.rank
        yield self.country
        yield self.city
        yield self.address
        yield self.hotel_tel
        yield self.hotel_remark

    class Meta:
        managed = False
        db_table = 'traval'
        verbose_name = '호텔'
        verbose_name_plural = '호텔 목록'

class ScheduleMaster(commonModel):
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=100, verbose_name='상품명')
    agent= models.ForeignKey(Agent, db_column='AGENT', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='여행사')
    manager = models.ForeignKey(Manager, db_column='MANAGER', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='담당자')
    location = models.CharField(db_column='LOCATION', max_length=100, verbose_name='지역')
    start = models.CharField(db_column='START', max_length=100, verbose_name='출발지')
    arrival = models.CharField(db_column='ARRIVAL', max_length=100, verbose_name='도착지')
    night = models.CharField(db_column='NIGHT', max_length=100, verbose_name='NIGHT')
    day = models.CharField(db_column='DAY', max_length=100, verbose_name='DAY')
    bus = models.CharField(db_column='BUS', max_length=100, verbose_name='버스')
    entrance = models.CharField(db_column='ENTRANCE', max_length=1000, verbose_name='입장지')
    breakfast = models.CharField(db_column='BREAKFAST', max_length=100, verbose_name='조식')
    lunch = models.CharField(db_column='LUNCH', max_length=100, verbose_name='중식')
    dinner = models.CharField(db_column='DINNER', max_length=100, verbose_name='석식')
    special = models.CharField(db_column='SPECIAL', max_length=1000, verbose_name='특식')
    option = models.CharField(db_column='OPTION', max_length=1000, verbose_name='옵션')
    shopping = models.CharField(db_column='SHOPPING', max_length=1000, verbose_name='쇼핑')
    schedule_remark = models.TextField(db_column='SCHEDULE_REMARK', max_length=1000, verbose_name='REMARK')
    
    def __str__(self):
        return f"{self.agent} - {self.agent.agent_name}, {self.manager} - {self.manager.manager_name}"
    
    def __iter__(self):
        yield self.product_name
        yield self.agent.agent_name
        yield self.manager.manager_name
        yield self.location
        yield self.start
        yield self.arrival
        yield self.night
        yield self.day
        yield self.schedule_remark

    class Meta:
        managed = False
        db_table = 'schedule_master'
        verbose_name = '스케줄 마스터'
        verbose_name_plural = '스케줄 마스터 목록'       

class ScheduleDetail(commonModel):
    master_id = models.ForeignKey(ScheduleMaster, db_column='MASTER_ID', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='마스터 ID')
    day = models.CharField(db_column='DAY', max_length=100, verbose_name='일차')
    schedule = models.CharField(db_column='SCHEDULE', max_length=100, verbose_name='일정')
    hotel = models.CharField(db_column='HOTEL', max_length=100, verbose_name='호텔')

    def __str__(self):
        return f"{self.master_id} - {self.master_id.product_name}"

    def __iter__(self):
        yield self.master_id
        yield self.day
        yield self.schedule
        yield self.hotel

    class Meta:
        managed = False
        db_table = 'schedule_detail'
        verbose_name = '스케줄 디테일'
        verbose_name_plural = '스케줄 디테일 목록'       

class Citycode(commonModel):
    country_name = models.CharField(db_column='COUNTRY_NAME', max_length=100, verbose_name='국가명')
    country_en_name = models.CharField(db_column='COUNTRY_EN_NAME', max_length=100, verbose_name='국가명(영문)')
    city_name = models.CharField(db_column='CITY_NAME', max_length=100, verbose_name='도시명')
    city_en_name = models.CharField(db_column='CITY_EN_NAME', max_length=100, verbose_name='도시명(영문)')
    city_code = models.CharField(db_column='CITY_CODE', max_length=100, verbose_name='도시코드')
    city_remark = models.TextField(db_column='CITY_REMARK', max_length=100, verbose_name='리마크')
    
    def __iter__(self):
        yield self.country_name
        yield self.country_en_name
        yield self.city_name
        yield self.city_en_name
        yield self.city_code
        yield self.city_remark

    class Meta:
        managed = False
        db_table = 'citycode'
        verbose_name = '국가 및 도시코드'
        verbose_name_plural = '국가 및 도시코드 목록'       


class Tourconductor(commonModel):
    tc_company = models.CharField(db_column='TC_COMPANY', max_length=100, verbose_name='소속회사')
    tc_name = models.CharField(db_column='TC_NAME', max_length=100, verbose_name='이름')
    tc_name_en = models.CharField(db_column='TC_NAME_EN', max_length=100, verbose_name='영문명')
    tc_tel = models.CharField(db_column='TC_TEL', max_length=100, verbose_name='연락처')
    passport_no = models.CharField(db_column='PASSPORT_NO', max_length=100, verbose_name='여권번호')
    rrno = models.CharField(db_column='RRNO', max_length=20, verbose_name='주민등록번호')
    tc_sex = models.CharField(db_column='TC_SEX', max_length=3, verbose_name='성별')
    tc_birth = models.CharField(db_column='TC_BIRTH', max_length=10, verbose_name='생년월일')
    tc_expiry = models.CharField(db_column='TC_EXPIRY', max_length=10, verbose_name='만료일')
    tc_modeid = models.CharField(db_column='TC_MODEID', max_length=30, verbose_name='모두ID')
    radio = models.CharField(db_column='RADIO', max_length=100, verbose_name='수신기')
    tc_mail = models.CharField(db_column='TC_MAIL', max_length=100, verbose_name='E-MAIL')
    tc_remark = models.TextField(db_column='TC_REMARK', max_length=100, verbose_name='리마크')
    
    def __iter__(self):
        yield self.tc_company
        yield self.tc_name
        yield self.tc_name_en
        yield self.tc_tel
        yield self.passport_no
        yield self.tc_sex
        yield self.tc_birth
        yield self.tc_modeid
        yield self.radio
        yield self.tc_remark

    class Meta:
        managed = False
        db_table = 'tourconductor'
        verbose_name = 'T/C'
        verbose_name_plural = 'T/C 목록'       


