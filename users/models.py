from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=16,default='')
    last_name = models.CharField(max_length=16,default='')
    info = models.CharField(max_length=255,default='')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username


