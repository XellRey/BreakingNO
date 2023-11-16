from django.db import models
from account.models import CustomUser
# Create your models here.


class Statement(models.Model):
    name = models.CharField(max_length=100)
    car_num = models.CharField(max_length=70)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=50, null=True, default='Under Consideration')

    def __str__(self):
        return self.name
