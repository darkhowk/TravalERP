from django.views import generic
from .common_models import Menu, commonModel
import math
from django.shortcuts import render

class CommonView(generic.ListView):
    title_nm = ""
    descript = ""
    template_name = ""
    menu_type = ""
    target = ""
    type = ""
    def __init__(self):
        self.topMenu = Menu.objects.filter(menu_type="TOP")
        self.leftMenu = Menu.objects.filter(menu_type="LEFT")
        self.tr_list = []

    def get(self, request, *args, **kwargs):
        self.per_page = int(request.GET.get('perPage', 5))
        self.current_page = int(request.GET.get('paging', 1))
        queryset = self.get_queryset()

        # 각 필드의 verbose_name을 tr_list에 추가
        for field in queryset.first()._meta.fields:
            tmp = True
            for common in commonModel._meta.fields:
                if field.verbose_name == common.verbose_name:
                    tmp = False
                elif  field.verbose_name in ['ID', 'TYPE']:
                    tmp = False
            
            if tmp == True:
                self.tr_list.append(field.verbose_name)

        # 그려질 페이지 목록
        self.content_list = queryset[self.per_page * (self.current_page - 1):self.per_page * self.current_page]

        # 페이지 수
        num_pages = math.ceil(queryset.count() / self.per_page)

        # 페이지 번호 목록
        self.pages = range(1, num_pages + 1)

        # 전체 아이템 갯수
        total_count = queryset.count()
        start_index = ((self.current_page - 1) * self.per_page) + 1
        end_index = (start_index + self.content_list.count()) - 1

        # 데이터들을 담는다
        self.content = {
            "descript": self.descript,
            "title_nm": self.title_nm,
            "topMenu": self.topMenu,
            "leftMenu": self.leftMenu,
            "content_list": self.content_list,
            "tr_list": self.tr_list,
            'pages': self.pages,
            'current_page': int(self.current_page),
            'per_page': int(self.per_page),
            'total_count': total_count,
            'start_index': start_index,
            'end_index': end_index,
            'target': self.target,
            'type': self.type,
        }
        return render(request, self.template_name, self.content)


class addView(generic.CreateView):
    def __init__(self):
        self.title_nm = ""
        self.descript = ""
        self.template_name = ""
        self.topMenu = Menu.objects.filter(menu_type="TOP")
        self.leftMenu = Menu.objects.filter(menu_type="LEFT")