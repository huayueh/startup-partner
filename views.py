from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def partner(request):
    return render(request, 'base.html')

def business(request):
    return render(request, 'business.html')
# def addperson(request):
#     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#     user.save()
#     person = Person()
#     person.name = 'harvey'
#     person.pid = '1234'
#     person.save()
#     return viewperson(request)
#
# def viewperson(request):
#     user_list = User.objects.all()
#     context = {'user_list': user_list}
#     person_list = Person.objects.all()
#     context.update({'person_list': person_list})
#     return render(request, 'polls/person.html', context)