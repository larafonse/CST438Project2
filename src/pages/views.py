from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def resgisterPage(request):
    context = {}
    return render(request, 'templates/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'templates/login.html', context)

def home_view(*args, **kwargs):
    return HttpResponse("Hello World")