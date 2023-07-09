from django.db import models
import datetime #Will be used when we have to check time after which we'll have to take charges  from the user.
from main.models import *
from django.conf import settings

# Create your models here.
class admin_control(models.Model):
    user = models.OneToOneField(
            User,
            default=None,
            null=True,
            on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Name)
