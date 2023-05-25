from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "POST":
        username = request.POST['userId']
        password = request.POST['userPassword']
        
        if username and password:  # 입력된 값이 존재하는지 확인
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/dashboard/')
            else:
                error = '아이디와 패스워드가 일치하지 않습니다.'
                return render(request, 'users/login.html', {'error': error})
        else:
            error = '아이디와 패스워드를 입력해주세요.'
            return render(request, 'users/login.html', {'error': error})
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/users/login.html')