from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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
    

class NASStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None, **kwargs):
        super().__init__(location, base_url, **kwargs)
        self.host = settings.NAS_HOST
        self.port = settings.NAS_PORT
        self.username = settings.NAS_USERNAME
        self.password = settings.NAS_PASSWORD

    def save(self, name, content, max_length=None):
        return super().save(name, content, max_length)

    def url(self, name):
        return 'http://{}:{}/{}'.format(self.host, self.port, name)


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        storage = NASStorage()
        file_path = storage.save(file.name, file)
        return HttpResponseRedirect('succ')
    else:
        return render(request, 'error.html')


def upload_file_success(request):
    return render(request, 'upload_file.html')