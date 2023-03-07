from django.shortcuts import render
from django.views import generic
# Create your views here.

class index(generic.ListView):
    def __init__(self):
        self.title_nm       = "설정페이지입니다."
        self.ogImgUrl       = ""
        self.descript       = "설정페이지입니다."
        self.template_name  = "setting/index.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":"[[[[ setting page ]]]]"}

        return render(request, self.template_name, self.content)