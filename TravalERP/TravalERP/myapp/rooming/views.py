from django.shortcuts import render
from django.views import generic

# Create your views here.


class firstIndex(generic.ListView):
    def __init__(self):
        self.title_nm       = "TON TOUR"
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "index.html"

    def get(self, request, *args, **kwargs):
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                                               
                        "dataList":""}

        return render(request, self.template_name, self.content)
    


class roomingIndex(generic.ListView):
    def __init__(self):
        self.title_nm       = "루밍"
        self.ogImgUrl       = ""
        self.descript       = "루밍"
        self.template_name  = "rooming/index.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":""}

        return render(request, self.template_name, self.content)
    