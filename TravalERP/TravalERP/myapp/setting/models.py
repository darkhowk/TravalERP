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
    id = models.IntegerField(db_column='ID', primary_key=True,)  # Field name made lowercase.
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