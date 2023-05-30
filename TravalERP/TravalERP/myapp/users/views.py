from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth, messages
from django.urls import reverse_lazy

def login(request):
    if request.method == "POST":
        username = request.POST['userId']
        password = request.POST['userPassword']
        
        if username and password:  # 입력된 값이 존재하는지 확인
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if password == 'ton12345':
                    return redirect('/changePw/')
                else:
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



class change_password(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url=reverse_lazy('dashboard:대시보드')
    template_name = 'users/changePw.html'

    def form_valid(self, form): 
        messages.success(self.request, '암호를 변경했습니다.') 
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "다시 시도해주시기 바랍니다.")
        return super(). form_invalid(form)


    