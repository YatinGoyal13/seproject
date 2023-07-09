from django.db import models
import datetime #Will be used when we have to check time after which we'll have to take charges  from the user.
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    startUpName = models.CharField(max_length=200, null=True,blank=True)
    founder = models.CharField(max_length=200, null=True,blank=True)
    email = models.CharField(max_length=2000, null=True,blank=True)
    description = models.CharField(max_length=2000, null=True,blank=True)
    pitch_link = models.CharField(max_length=2000, null=True,blank=True)
    video_link = models.CharField(max_length=2000, null=True,blank=True)
    type_of_incorporation = models.CharField(max_length=2000, null=True,blank=True)
    name_of_legal_entity = models.CharField(max_length=2000, null=True,blank=True)
    Directors_Partners = models.CharField(max_length=2000, null=True,blank=True)
    Funding_status = models.BooleanField(max_length=2000, null=True,blank=True)
    Funding_requirements = models.PositiveIntegerField(null=True,blank=True)
    Registered_address = models.CharField(max_length=2000, null=True,blank=True)
    Website = models.CharField(max_length=2000, null=True,blank=True)
    Socia_media_links = models.CharField(max_length=2000, null=True,blank=True)
    founders_email = models.EmailField(max_length=2000, null=True,blank=True)
    PAN = models.PositiveIntegerField(null=True,blank=True)
    Account_No_Bank = models.PositiveIntegerField(null=True,blank=True)
    Name_of_bank = models.CharField(max_length=2000,null=True,blank=True)
    info_filled = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.startUpName)
