from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer=models.BooleanField(default=False)
    name=models.CharField(max_length=250,null=True)
    phonenumber=models.IntegerField(null=True)
    address=models.CharField(max_length=250,null=True)

class stock(models.Model):
    items=models.CharField(max_length=250,null=True)
    price=models.IntegerField()
    photo = models.ImageField(upload_to='photo', null=True, blank=True)


