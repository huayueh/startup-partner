from django.shortcuts import render
from partner.models import UserProfile


def partner(request):
    profile_list = UserProfile.objects.all()
    context = {'profile_list': profile_list}
    return render(request, 'partner/partner.html', context)

def view_profile(request):
    p, created = UserProfile.objects.get_or_create(username=request.user.username)
    context = {'profile': p}
    return render(request, 'partner/partner_profile.html', context)

def edit_profile(request):
    public = request.POST['public']
    website = request.POST['website']
    location = request.POST['location']
    skill_type = request.POST['skill_type']
    skill_detail = request.POST['skill_detail']
    contact_info = request.POST['contact_info']

    p, created = UserProfile.objects.get_or_create(username=request.user.username)
    p.public = bool(public)
    p.website = str(website).replace('http://', '')
    p.location = location
    p.skill_type = skill_type
    p.skill_detail = skill_detail
    p.contact_info = contact_info
    p.save()

    return view_profile(request)
