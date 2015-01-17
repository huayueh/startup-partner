from django.utils import timezone
from django.shortcuts import render
from business.models import Business
from partner.models import UserProfile


def business(request):
    biz_list = Business.objects.all().order_by('-pub_date')
    context = {"biz_list" : biz_list}
    return render(request, 'business/business.html', context)

def business_search(request):
    return business(request)

def view_category(request):
    type = request.GET['type']
    biz_list = Business.objects.all().filter(industry=type).order_by('-pub_date')
    context = {"biz_list": biz_list}
    return render(request, 'business/business.html', context)

def add_business(request):
    p = UserProfile.objects.get(username=request.user.username)
    context = {'profile': p}
    return render(request, 'business/add_business.html', context)

def business_detail(request):
    id = request.GET['id']
    biz = Business.objects.get(pk=id)
    context = {'biz': biz}
    return render(request, 'business/business_detail.html', context)

def insert_business(request):
    user = request.user.username
    title = request.POST['title']
    industry = request.POST['industry']
    location = request.POST['location']
    content = request.POST['content']
    try:
        user_profile = UserProfile.objects.get(username=user)
        contact_info = user_profile.contact_info
    except UserProfile.DoesNotExist:
        contact_info = ''

    b = Business(title=title, industry=industry, location=location, content=content, contact_info=contact_info, pub_date=timezone.now())
    b.save()
    return business(request)

