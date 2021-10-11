"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # User Pages
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('userProfile/', views.userPage, name="user"),
    # path('admin/createUser', views.adminCreateAccountPage, name="createUser"),
    path('allItems/', views.allItemsPage, name="allItems"),
    path('editUser/', views.editUserPage, name="editUsers"),
    path('item/', views.itemPage, name="item"),
    


    # Admin pages
    path('adminAllUsers/', views.allUsersPage, name="allUsers"),


    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
