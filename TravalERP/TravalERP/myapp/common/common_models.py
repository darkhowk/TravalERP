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
    menu = models.CharField(db_column='MENU', primary_key=True, max_length=10, verbose_name='메뉴')  # Field name made lowercase.
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
    agent_type = models.CharField(db_column='AGENT_TYPE', max_length=100, verbose_name='여행사 종류')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agent'
        verbose_name = '여행사'
        verbose_name_plural = '여행사 목록'

class Manager(commonModel):
    agent= models.ForeignKey(Agent, db_column='agent', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='여행사')
    manager_name= models.CharField(db_column='MANAGER_NAME', max_length=100, verbose_name='담당자명')  # Field name made lowercase.
    manager_tel= models.CharField(db_column='MANAGER_TEL', max_length=20, verbose_name='담당자 연락처')  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=100, verbose_name='담당자 종류')  # Field name made lowercase.
    manager_hp = models.CharField(db_column='MANAGER_HP', max_length=100, verbose_name='담당자 휴대폰')  # Field name made lowercase.
    manager_messenger = models.CharField(db_column='MANAGER_MESSENGER', max_length=100, verbose_name='담당자 메신저')  # Field name made lowercase.
    manager_email = models.CharField(db_column='MANAGER_EMAIL', max_length=100, verbose_name='담당자 이메일')  # Field name made lowercase.
    manager_remark = models.TextField(db_column='MANAGER_REMARK', max_length=1000, blank=True, null=True, verbose_name='REMARK')  # Field name made lowercase.

    def __str__(self):
        return f"{self.agent} - {self.agent.agent_name}"
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
    arrival_time = models.CharField(db_column='ARRIVAL_TIEM', max_length=100, verbose_name='도착시간')
    time_taken = models.TextField(db_column='TIME_TAKEN', max_length=1000, verbose_name='소요시간')
    manager = models.ForeignKey(Manager, db_column='MANAGER', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='담당자')
    airport_remark = models.TextField(db_column='AIRPORT_REMARK', max_length=1000, blank=True, null=True, verbose_name='REMARK')

    def __str__(self):
        return f"{self.manager} - {self.manager.manager_name}"
    class Meta:
        managed = False
        db_table = 'airport'
        verbose_name = '항공'
        verbose_name_plural = '항공 목록'