from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .models import User
from .forms import CreateUserForm
from .forms import ItemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import allowed_users, unauthenticated_user

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerPage(request):
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

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/' + str(request.user.id))
        else:
            messages.info(request, 'username OR password incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
def homePage(request, pk):
    context = {}
    return render(request, 'pages/home.html', context )

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
def userPage(request):
    context = {}
    return render(request, 'pages/user.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def allUsersPage(request):
    all_users = User.objects.all
    context = {'all_users': all_users}
    return render(request, 'pages/allUsers.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def adminCreateAccountPage(request):
    context = {}
    return render(request, 'pages/adminCreateAcc.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
def editUserPage(request):
    context = {}
    return render(request, 'pages/editUsers.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
def itemPage(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/allItems')

    context = {'form': form}
    return render(request, 'pages/item.html', context)

@unauthenticated_user
# @allowed_users(allowed_roles=['admin','user'])
def landingPage(request):
    context = {}
    return render(request, 'pages/Landing.html', context)
  
@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
def allItemsPage(request, pk):
    wishlist = Item.objects.filter(customerId=pk)
    context = {'wishlist':wishlist}
    return render(request, 'pages/allItems.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
def individualItem(request, pk):
    wishlist = Item.objects.filter(id=pk)
    context = {'item':wishlist[0]}
    return render(request, 'pages/individualItem.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
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

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','user'])
def delete(request, pk):
    userItem = Item.objects.get(id=pk)
    if request.method == "POST":
        userItem.delete()
        return redirect('/allItems/' + str(pk))
        
    context = {'item' : userItem}
    return render(request, 'pages/delete.html', context)