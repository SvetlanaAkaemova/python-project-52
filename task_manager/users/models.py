from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractUser):

#class User(AbstractBaseUser):
#    username = models.CharField(max_length=150)
#    first_name = models.CharField(max_length=150)
#    last_name = models.CharField(max_length=150)
#    created_at = models.DateTimeField(auto_now_add=True)
#    password = models.CharField(max_length=20)
#    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
