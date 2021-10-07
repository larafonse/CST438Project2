from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registerPage(request):
    context = {}
    return render(request, 'pages/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'pages/login.html', context)

def homePage(request):
    context = {}
    return render(request, 'pages/home.html', context )


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
    wishlist = [
        {
            "productName": "First List Item",
            "productDescription":"Onewheel is a self-balancing single wheel electric board-sport, recreational personal transporter, often described as an electric skateboard. Unlike the electric unicycle, the riders feet are typically pointed at a perpendicular angle to the wheel and direction of travel.",
            "id": 1,
            "imgURL":"https://cdn.shopify.com/s/files/1/0696/2011/t/98/assets/graphic-product-xr_800x400_crop_bottom.progressive.jpg?v=16559566961669616584"
        },
        {
            "productName": "Second List itme",
            "productDescription":"Onewheel is a self-balancing single wheel electric board-sport, recreational personal transporter, often described as an electric skateboard. Unlike the electric unicycle, the riders feet are typically pointed at a perpendicular angle to the wheel and direction of travel.",
            "id": 2,
            "imgURL":"https://cdn.shopify.com/s/files/1/0696/2011/t/98/assets/graphic-product-xr_800x400_crop_bottom.progressive.jpg?v=16559566961669616584"
        }]
    return render(request, 'pages/allItems.html', {"wishlist":wishlist})