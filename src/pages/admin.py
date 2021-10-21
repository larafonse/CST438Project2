from django.contrib import admin
from .models import  Item




class itemAdmin(admin.ModelAdmin):
    list_display = ['productName', 'productDescription' ]
    list_filter = ['customerId']


admin.site.register(Item, itemAdmin)

admin.site.site_header = "Wish List Admin"