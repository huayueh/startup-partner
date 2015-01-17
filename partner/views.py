from django.shortcuts import render
from django.utils import timezone
from partner.models import UserProfile


def partner(request):
    profile_list = UserProfile.objects.all().order_by('-last_modify')
    context = {'profile_list': profile_list}
    return render(request, 'partner/partner.html', context)

def partner_search(request):
    return partner(request)

def view_category(request):
    type = request.GET['type']
    profile_list = UserProfile.objects.all().filter(skill_type=type).order_by('-last_modify')
    context = {'profile_list': profile_list}
    return render(request, 'partner/partner.html', context)

def view_profile(request):
    p, created = UserProfile.objects.get_or_create(username=request.user.username)
    context = {'profile': p}
    return render(request, 'partner/partner_profile.html', context)

def user_detail(request):
    name = request.GET['name']
    p = UserProfile.objects.get(username=name)
    context = {'profile': p}
    return render(request, 'partner/partner_detail.html', context)

def edit_profile(request):
    public = request.POST['public']
    website = request.POST['website']
    location = request.POST['location']
    skill_type = request.POST['skill_type']
    skill_detail = request.POST['skill_detail']
    contact_info = request.POST['contact_info']

    p, created = UserProfile.objects.get_or_create(username=request.user.username)
    p.public = bool(public == 'true')
    p.website = str(website).replace('http://', '')
    p.location = location
    p.skill_type = skill_type
    p.skill_detail = ''.join(skill_detail.splitlines())
    p.contact_info = contact_info
    p.last_modify = timezone.now()
    p.save()

    return partner(request)
