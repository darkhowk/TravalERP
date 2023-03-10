from django.contrib import admin
from .common_models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('')
    list_filter = ('')
    search_fields = ('')
    

admin.site.register(Menu, MenuAdmin)
