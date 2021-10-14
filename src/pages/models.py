from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    productName = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=250)
    imgURL = models.CharField(max_length=500)
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName
    