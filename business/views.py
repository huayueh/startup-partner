from django.utils import timezone
from django.shortcuts import render
from business.models import Business


def business(request):
    return render(request, 'business/business.html')

def add_business(request):
    return render(request, 'business/add_business.html')

def insert_business(request):
    title = request.POST['title']
    industry = request.POST['industry']
    location = request.POST['location']
    content = request.POST['content']
    contact_info = request.POST['contact_info']
    b = Business(title=title, industry=industry, location=location, content=content, contact_info=contact_info, pub_date=timezone.now())
    b.save()
    return business(request)

