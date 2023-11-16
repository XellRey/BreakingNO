from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/', default='default/no-avatar.png')
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150)
    car_num = models.CharField(max_length=10)

