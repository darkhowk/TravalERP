from django import forms
from .common_models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('menu', 'menu_name', 'upper_menu')
        labels = {'menu': '메뉴', "menu_name" : '메뉴명', "upper_menu" : '상위메뉴'}
        widgets= {
                'menu' : forms.TextInput()
                }
