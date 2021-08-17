

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Accounts(AbstractUser):
    phone = models.CharField(max_length=50)
   
    REQUIRED_FIELDS = ['first_name', 'last_name']  