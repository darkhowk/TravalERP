from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth, messages

def login(request):
    if request.method == "POST":
        username = request.POST['userId']
        password = request.POST['userPassword']
        
        if username and password:  # 입력된 값이 존재하는지 확인
            if (password == 'ton12345'):
                   return redirect('/changePw/')
            else :
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

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 변경하였습니다.")
            return redirect("dashborad:index")
        else:
            form_errors = form.errors.as_data()
            error_message = form_errors.get("__all__")[0].message if form_errors.get("__all__") else "다시 시도해주세요."
            messages.error(request, error_message)
            
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'users/changePw.html',{'form':form})
    
    


    