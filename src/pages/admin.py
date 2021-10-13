from django.contrib import admin
from .models import User, Item

class wishListAdmin(admin.ModelAdmin):
    list_display = {'title', 'slug'}

class userAdmin(admin.ModelAdmin):
    list_display = {'firstName', 'lastName', 'customerId', }
    list_filter ={'firstName', }
    List_filter ={'customerId', }

class itemAdmin(admin.ModelAdmin):
    list_display = {'productName', 'productDescription', }
    list_filter = {'customerId'}


admin.site.register(User, userAdmin)
admin.site.register(Item, itemAdmin)

admin.site.site_header = "Wish List Admin"


