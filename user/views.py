from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import logout , authenticate , login
from django.contrib import messages
import re

User = get_user_model()

def login_view(request):
    if request.user.is_authenticated:
        return redirect('events:events_list')
    
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password )

        if user is not None :
            login(request , user)
            return redirect('events:events_list') 
        else :
            messages.error(request , '用戶名或密碼錯誤')

    return render (request , 'login.html')

def register(request):
    error = {}


    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            error['username'] = '使用者名稱已存在'
        elif User.objects.filter(email=email).exists():
            error['email'] = '電子郵件已存在'
        elif password1 != password2:
            error['password'] = '兩次密碼輸入不一樣'
       
        else:
            try:
                User.objects.create_user(username=username, password=password1, email=email)
                messages.success(request, '註冊成功，請登入')
                return redirect('user:login')
            except Exception as e:
                messages.error(request, f'註冊失敗：{str(e)}')

    return render(request, 'register.html' , {'error':error})

def logout_view(request):
    logout(request)
    return redirect('user:login')
    