from django.shortcuts import render
from django.views import generic
# Create your views here.

class tonproduct(generic.ListView):
    def __init__(self):
        self.title_nm       = "메인페이지입니다."
        self.ogImgUrl       = ""
        self.descript       = "메인페이지입니다."
        self.template_name  = "ton/product.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":"[[[[ Hellow DJango ]]]]"}

        return render(request, self.template_name, self.content)