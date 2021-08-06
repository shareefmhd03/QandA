

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Accounts(AbstractUser):
    phone = models.CharField(max_length=12, blank=True, null=True)
   

    REQUIRED_FIELDS = ['first_name', 'last_name']  