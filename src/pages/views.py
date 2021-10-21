from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .models import User
from .forms import CreateUserForm
from .forms import ItemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                userName = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + userName);

                return redirect('login')

    context = {'form': form}
    return render(request, 'pages/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username OR password incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def homePage(request):
    context = {}
    return render(request, 'pages/home.html', context )

def userPage(request):
    context = {}
    return render(request, 'pages/user.html', context)

def allUsersPage(request):
    all_users = User.objects.all
    context = {'all_users': all_users}
    return render(request, 'pages/allUsers.html', context)

def adminCreateAccountPage(request):
    context = {}
    return render(request, 'pages/adminCreateAcc.html', context)

def editUserPage(request):
    context = {}
    return render(request, 'pages/editUsers.html', context)

def itemPage(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/allItems')

    context = {'form': form}
    return render(request, 'pages/item.html', context)

def allItemsPage(request, pk):
    wishlist = Item.objects.filter(id=pk)
    context = {'wishlist':wishlist}
    return render(request, 'pages/allItems.html', context)

def update(request,pk):

    userItem = Item.objects.get(id=pk)
    form = ItemForm(instance=userItem)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=userItem)
        if form.is_valid():
            form.save()
            return redirect('/allItems/' + str(pk))
    context = {
        'form': form
    }
    return render(request, 'pages/update.html', context)


def delete(request, pk):
    userItem = Item.objects.get(id=pk)
    if request.method == "POST":
        userItem.delete()
        return redirect('/allItems/' + str(pk))
        
    context = {'item' : userItem}
    return render(request, 'pages/delete.html', context)