# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin
from ..common.common_models import Menu

class MenuView(admin.ModelAdmin):
    list_display  = ('menu', 'menu_name', 'upper_menu')
    list_filter   = ('use_yn', 'entry_date')
    search_fields = ('menu_name', 'upper_menu', 'use_yn')

admin.site.register(Menu, MenuView)