from django.db import models

# Create your models here.
class wishList(models.Model):
    title=models.CharField(max_length=200)
    slug =models.SlugField(unique=True)

class User(models.Model):
    customerId = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.customerId)



class Item(models.Model):
    productName = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=250)
    imgURL = models.CharField(max_length=500)
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName



