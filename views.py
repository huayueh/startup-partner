from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from business.models import Business


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def tinymce(request):
    return render(request, 'tinymce.html')

def test_tinymce(request):
    context = {'plain': request.POST.get('content', '')}
    return render(request, 'tinymce.html', context)

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'business/template/business/business.html')
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
        return viewperson(request)
    return HttpResponse('fail')

def viewperson(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'person.html', context)