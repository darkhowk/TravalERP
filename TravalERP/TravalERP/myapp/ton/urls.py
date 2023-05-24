# myapp/blog/urls.py

from django.urls import path
from . import views
from .views import upload_file

app_name = "ton"

urlpatterns = [    
    path("ton/", views.tonproduct.as_view(), name="기술서"),
    path('ton/upload/', upload_file, name='upload_file'),
]