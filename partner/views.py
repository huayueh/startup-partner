from django.shortcuts import render


def partner(request):
    return render(request, 'partner/partner.html')
