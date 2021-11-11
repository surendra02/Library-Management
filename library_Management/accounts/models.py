from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomerUserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,unique=True,blank=False,null=False)
    mobile=models.CharField(max_length=10,blank=True,null=True)
    status = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomerUserManager()

