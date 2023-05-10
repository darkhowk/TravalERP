from django.views import generic
from .common_models import Menu, commonModel, Agent
import math
from django.shortcuts import render
import json


class CommonMainView(generic.ListView):
    title_nm = ""
    descript = ""
    template_name = ""
    menu_type = ""
    target = ""
    type = ""

    def __init__(self):
        self.topMenu = Menu.objects.filter(menu_type="TOP", use_yn='Y')

    def get(self, request, *args, **kwargs):
        
        self.perPage = int(request.GET.get('perPage', '5'))
        self.paging = int(request.GET.get('paging', '1'))
        model, type, value  = self.custom_queryset()

        if type is None:
            queryset = model.objects.filter(use_yn='Y')
        else:
            queryset = model.objects.filter(type=value)

        self.content_list = queryset[self.perPage * (self.paging - 1):self.perPage * self.paging]

        # 페이지 수
        num_pages = math.ceil(queryset.count() / self.perPage)

        # 페이지 번호 목록
        self.pages = range(1, num_pages + 1)

        # 전체 아이템 갯수
        total_count = queryset.count()
        start_index = ((self.paging - 1) * self.perPage) + 1
        end_index = (start_index + self.content_list.count()) - 1

        # 데이터들을 담는다
        self.content = {
            "descript": self.descript,
            "title_nm": self.title_nm,
            "topMenu": self.topMenu,
            "content_list": self.content_list,
            'pages': self.pages,
            'paging': int(self.paging),
            'perPage': int(self.perPage),
            'total_count': total_count,
            'start_index': start_index,
            'end_index': end_index,
            'target': self.target,
            'type': self.type,
        }
        return render(request, self.template_name, self.content)

class CommonView(generic.ListView):
    title_nm = ""
    descript = ""
    template_name = "setting/commonSettingView.html"
    menu_type = ""
    target = ""
    type = ""

    def __init__(self):
        self.topMenu = Menu.objects.filter(menu_type="TOP", use_yn='Y')
        self.leftMenu = Menu.objects.filter(menu_type="LEFT", use_yn='Y')
        self.tr_list = []

    def get(self, request, *args, **kwargs):
        
        self.perPage = int(request.GET.get('perPage', '10'))
        self.paging = int(request.GET.get('paging', '1'))
        model, type, value  = self.custom_queryset()

        if type is None:
            queryset = model.objects.all()
        else:
            queryset = model.objects.filter(type=value)

        if queryset.first() is None:
            # 각 필드의 verbose_name을 tr_list에 추가

            for field in model._meta.fields:
                tmp = True
                for common in commonModel._meta.fields:
                    if field.verbose_name == common.verbose_name:
                        tmp = False
                    elif field.verbose_name in ['ID', 'TYPE', 'E-MAIL', '주민등록번호', '만료일', '버스', '입장지', '조식', '중식', '석식', '특식', '옵션', '쇼핑','주소', '웹사이트']:
                        tmp = False
                if tmp:
                    self.tr_list.append(field.verbose_name)

        else:
            # 각 필드의 verbose_name을 tr_list에 추가
            for field in queryset.first()._meta.fields:
                tmp = True
                for common in commonModel._meta.fields:
                    if field.verbose_name == common.verbose_name:
                        tmp = False
                    elif field.verbose_name in ['ID', 'TYPE', 'E-MAIL', '주민등록번호', '만료일', '버스', '입장지', '조식', '중식', '석식', '특식', '옵션', '쇼핑', '주소', '웹사이트' ]:
                        tmp = False
                if tmp:
                    self.tr_list.append(field.verbose_name)

        ## 여행사 로컬명등의 tr네임 바꾸기
        if (self.target == 'agent' and self.type != 'A') or  (self.target == 'manager' and self.type != 'M'):
            for i, val in enumerate(self.tr_list):
                if val == '여행사':
                    self.tr_list[i] = '로컬명'
                    
        self.content_list = queryset[self.perPage * (self.paging - 1):self.perPage * self.paging]

        # 페이지 수
        num_pages = math.ceil(queryset.count() / self.perPage)

        # 페이지 번호 목록
        self.pages = range(1, num_pages + 1)

        # 전체 아이템 갯수
        total_count = queryset.count()
        start_index = ((self.paging - 1) * self.perPage) + 1
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
            'paging': int(self.paging),
            'perPage': int(self.perPage),
            'total_count': total_count,
            'start_index': start_index,
            'end_index': end_index,
            'target': self.target,
            'type': self.type,
        }
        return render(request, self.template_name, self.content)

class addView(generic.CreateView):
    title_nm = ""
    descript = ""
    #공통변수
    paging = ""
    perPage = ""
    target = ""
    type = ""
    pageType = ""

    def __init__(self):
        self.topMenu = Menu.objects.filter(menu_type="TOP", use_yn='Y')
        self.leftMenu = Menu.objects.filter(menu_type="LEFT", use_yn='Y')

    def get(self, request, *args, **kwargs):
        #선택 데이터
        selectData = self.seletData()
        
        #옵션에 그려질 데이터
        optionData = self.selectOption(request) or {}

        #공통변수
        self.paging = request.GET.get('paging')
        self.perPage = request.GET.get('perPage')
        self.target = request.GET.get('target')
        self.type = request.GET.get('type')
        self.pageType = request.GET.get('pageType')

        # 데이터들을 담는다
        self.content = {
            "descript": self.descript,
            "title_nm": self.title_nm,
            "topMenu": self.topMenu,
            "leftMenu": self.leftMenu,
            'paging': int(self.paging),
            'perPage': int(self.perPage),
            'target': self.target,
            'type': self.type,
            'pageType' : self.pageType,
            'selectData': selectData,
            'optionData': optionData,
        }
        return render(request, self.template_name, self.content)
    
class CommonMainAddView(generic.CreateView):
    title_nm = ""
    descript = ""
    #공통변수
    paging = ""
    perPage = ""
    target = ""
    type = ""
    pageType = ""

    def __init__(self):
        self.topMenu = Menu.objects.filter(menu_type="TOP", use_yn='Y')

    def get(self, request, *args, **kwargs):
        #선택 데이터
        selectData = self.seletData()
        
        #옵션에 그려질 데이터
        optionData = self.selectOption(request) or {}

        #공통변수
        self.paging = request.GET.get('paging')
        self.perPage = request.GET.get('perPage')
        self.target = request.GET.get('target')
        self.type = request.GET.get('type')
        self.pageType = request.GET.get('pageType')

        # 데이터들을 담는다
        self.content = {
            "descript": self.descript,
            "title_nm": self.title_nm,
            "topMenu": self.topMenu,
            'paging': int(self.paging),
            'perPage': int(self.perPage),
            'target': self.target,
            'type': self.type,
            'pageType' : self.pageType,
            'selectData': selectData,
            'optionData': optionData,
        }
        return render(request, self.template_name, self.content)