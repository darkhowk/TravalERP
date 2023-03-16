# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin

class Agent(models.Model):
    agent_name= models.CharField(db_column='AGENT_NAME', max_length=100)  # Field name made lowercase.
    agent_tel= models.CharField(db_column='AGENT_TEL', max_length=100)  # Field name made lowercase.
    agent_type = models.CharField(db_column='AGENT_TYPE', max_length=100)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=100)  # Field name made lowercase.
    entry_id = models.CharField(db_column='ENTRY_ID', max_length=20)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    updat_id = models.CharField(db_column='UPDAT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updat_date = models.DateTimeField(db_column='UPDAT_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agent'

class Manager(models.Model):
    agent_name= models.CharField(db_column='AGENT_NAME', max_length=100)  # Field name made lowercase.
    manager_name= models.CharField(db_column='MANAGER_NAME', max_length=100)  # Field name made lowercase.
    manager_tel= models.CharField(db_column='MANAGER_TEL', max_length=20)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=100)  # Field name made lowercase.
    manager_hp = models.CharField(db_column='MANAGER_HP', max_length=100)  # Field name made lowercase.
    manager_messenger = models.CharField(db_column='MANAGER_MESSENGER', max_length=100)  # Field name made lowercase.
    manager_email = models.CharField(db_column='MANAGER_EMAIL', max_length=100)  # Field name made lowercase.
    manager_remark = models.TextField(db_column='MANAGER_REMARK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=100)  # Field name made lowercase.
    entry_id = models.CharField(db_column='ENTRY_ID', max_length=20)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    updat_id = models.CharField(db_column='UPDAT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updat_date = models.DateTimeField(db_column='UPDAT_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manager'

class Airport(models.Model):
    airport_name= models.CharField(db_column='AIRPORT_NAME', max_length=100)  # Field name made lowercase.
    departure_airport= models.CharField(db_column='DEPARTURE_AIRPORT', max_length=100)  # Field name made lowercase.
    departure_city = models.CharField(db_column='DEPARTURE_CITY', max_length=100)  # Field name made lowercase.
    departure_time = models.CharField(db_column='DEPARTURE_TIME', max_length=100)  # Field name made lowercase.
    arrival_airport= models.CharField(db_column='ARRIVAL_AIRPORT', max_length=100)  # Field name made lowercase.
    arrival_city = models.CharField(db_column='ARRIVAL_CITY', max_length=100)  # Field name made lowercase.
    arrival_time = models.CharField(db_column='ARRIVAL_TIEM', max_length=100)  # Field name made lowercase.
    time_taken = models.TextField(db_column='TIME_TAKEN', max_length=1000)  # Field name made lowercase.
    manager = models.ForeignKey(Manager, db_column='MANAGER', on_delete=models.SET_NULL, blank=True, null=True)
    airport_remark = models.TextField(db_column='AIRPORT_REMARK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=100)  # Field name made lowercase.
    entry_id = models.CharField(db_column='ENTRY_ID', max_length=20)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    updat_id = models.CharField(db_column='UPDAT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updat_date = models.DateTimeField(db_column='UPDAT_DATE', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.manager} - {self.manager.manager_name}"
    class Meta:
        managed = True
        db_table = 'airport'