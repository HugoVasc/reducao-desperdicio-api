from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(unique=True, blank=False) 
    username = models.CharField(max_length=20, unique=True, blank=True)
    phone = models.CharField(max_length=15)
    def __str__(self):
        display_user = {
            'username': self.username,
            'name': self.first_name + ' ' + self.last_name,
            'email': self.email,
            'phone': self.phone,
        }
        return str(display_user)
    pass