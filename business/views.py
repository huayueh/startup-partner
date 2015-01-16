from django.utils import timezone
from django.shortcuts import render
from business.models import Business
from partner.models import UserProfile


def business(request):
    biz_list = Business.objects.all()
    context = {"biz_list" : biz_list}
    return render(request, 'business/business.html', context)

def add_business(request):
    p = UserProfile.objects.get(username=request.user.username)
    context = {'profile': p}
    return render(request, 'business/add_business.html', context)

def business_detail(request):
    id = request.GET['id']
    biz = Business.objects.get(pk=id)
    try:
        contact_info = UserProfile.objects.get(username=biz.post_user)
    except UserProfile.DoesNotExist:
        contact_info = ''
    context = {'biz': biz, 'contact_info': contact_info}
    return render(request, 'business/business_detail.html', context)

def insert_business(request):
    user = request.user.username
    title = request.POST['title']
    industry = request.POST['industry']
    location = request.POST['location']
    content = request.POST['content']
    b = Business(post_user=user, title=title, industry=industry, location=location, content=content, pub_date=timezone.now())
    b.save()
    return business(request)

