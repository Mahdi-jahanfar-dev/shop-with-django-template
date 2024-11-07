from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone_number = models.IntegerField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    USERNAME_FIELD = ['email', 'phone_number']
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.email