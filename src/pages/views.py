from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm;
# Create your views here.

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'pages/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'pages/login.html', context)

def homePage(request):
    context = {}
    return render(request, 'pages/home.html', context)

def userPage(request):
    context = {}
    return render(request, 'pages/user.html', context)

def allUsersPage(request):
    context = {}
    return render(request, 'pages/allUsers.html', context)

def adminCreateAccountPage(request):
    context = {}
    return render(request, 'pages/adminCreateAcc.html', context)

def editUserPage(request):
    context = {}
    return render(request, 'pages/editUsers.html', context)

def itemPage(request):
    context = {}
    return render(request, 'pages/item.html', context)

def allItemsPage(request):
    context = {}
    return render(request, 'pages/allItems.html', context)