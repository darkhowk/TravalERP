from django.urls import path
from . import views

app_name = "ajax"

urlpatterns = [    
    path("ajax/get/<str:item>", views.getData, name="ajax검색"), 
    path("ajax/getLike/<str:item>", views.getLikeData, name="ajax Like 검색"), 
    path("ajax/fileupload/<str:item>", views.file_upload, name="ajax 파일 업로드"), 
    path("ajax/excelUpload/<str:item>", views.excelUpload, name="ajax 엑셀 업로드"), 
    path("ajax/getREF/<str:target>", views.getREF, name="ajax REF검색"), 
    path("ajax/searchREF", views.searchREF, name="ajax REF검색(수정,삭제용)"), 
    path("ajax/searchDetail", views.searchDetail, name="ajax Detail검색(수정,삭제용)"), 
    

    ### copy Data
    path("ajax/copyData", views.dataCopy, name="데이터 카피 ajax"),

    #### 공통 ajax
    path("ajax/insertData/<str:item>", views.dataInsert, name="등록 ajax"),
    path("ajax/updateData/<str:item>", views.dataUpdate, name="수정 ajax"),
    path("ajax/deleteData/<str:item>", views.dataDelete, name="삭제 ajax"),

    ##### Master Detail ajax
    path("ajax/insertData/master/<str:item>", views.masterInsert, name="master등록 ajax"),
    path("ajax/insertData/detail/<str:item>", views.detailInsert, name="detail등록 ajax"),
    path("ajax/updateData/master/<str:item>", views.masterUpdate, name="master수정 ajax"),
    path("ajax/updateData/detail/<str:item>", views.detailupdate, name="detail수정 ajax"),
    path("ajax/deletaData/master/<str:item>", views.masterDelete, name="master삭제 ajax"),
    path("ajax/deleteData/detail/<str:item>", views.detailDelete, name="detail삭제 ajax"),

]
