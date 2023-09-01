from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request):
    context={'page':'home'}
    return render(request,"portfolio/index.html",context)


def about(request):
    context={'page':'about'}
    return render(request,"portfolio/about-us.html",context)

def services(request):
    context={'page':'about'}
    return render(request,"portfolio/services.html",context)

def contact(request):
    context={'page':'about'}
    return render(request,"portfolio/contact.html",context)