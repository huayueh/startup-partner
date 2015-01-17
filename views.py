from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'business/business.html')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def user_logout(request):
    logout(request)
    return render(request, 'index.html')

def check_user_exist(request):
    name = request.REQUEST['userName']
    response_data = 'false'
    # pass check if not exist
    if not User.objects.filter(username = name).exists():
        response_data = 'true'
    return HttpResponse(response_data)

def add_user(request):
    name = request.REQUEST['userName']
    email = request.REQUEST['userEmail']
    pwd = request.REQUEST['pwd']

    if not User.objects.filter(username = name).exists():
        user = User.objects.create_user(name, email, pwd)
        user.save()

        return index(request)
    return HttpResponse('fail')
