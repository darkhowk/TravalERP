from django.shortcuts import render
from django.views import generic
# Create your views here.

class loginIndex(generic.ListView):
   def __init__(self):
        self.title_nm = "login"
        self.ogImgUrl = ""
        self.descript = "login"
        self.template_name = "login/index.html"

      
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                     }

      return render(request, self.template_name, self.content)
   

class loginPwr(generic.ListView):
   def __init__(self):
      self.title_nm = "login password"
      self.ogImgUrl = ""
      self.descript = "password"
      self.template_name = "login/pwr.html"
   def get(self, request, *args, **kwargs):
      self.content = {
                        "descript" : self.descript,
                        "title_nm" : self.title_nm,
                        "ogImgUrl" : self.ogImgUrl,
                     }

      return render(request, self.template_name, self.content)