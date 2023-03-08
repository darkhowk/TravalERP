from django.db import models

# Create your models here.
class Menu(models.Model):
    menu = models.CharField(db_column='MENU', primary_key=True, max_length=10)  # Field name made lowercase.
    menu_name = models.CharField(db_column='MENU_NAME', max_length=100)  # Field name made lowercase.
    upper_menu = models.CharField(db_column='UPPER_MENU', max_length=10, blank=True, null=True)  # Field name made lowercase. 
    use_yn = models.CharField(db_column='USE_YN', max_length=100)  # Field name made lowercase.
    entry_id = models.CharField(db_column='ENTRY_ID', max_length=20)  # Field name made lowercase.
    entry_date = models.DateField(db_column='ENTRY_DATE')  # Field name made lowercase.
    updat_id = models.CharField(db_column='UPDAT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.     
    updat_date = models.DateField(db_column='UPDAT_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'