from django.contrib.auth.forms import UserCreationForm
#from pyrsistent import v
from .models import *
from django import forms
from django.core.exceptions import ValidationError
import datetime

class UserForm(UserCreationForm):
    password1 = forms.CharField(min_length=8, max_length=30, widget=forms.PasswordInput(render_value=False))
    class Meta:
        model = User
        fields = ['username' ,'password1', 'password2','startUpName','founder','email','description','pitch_link','video_link']

class UserForm_login(forms.Form):
    type_of_incorporation = forms.CharField()
    name_of_legal_entity = forms.CharField()
    Directors_Partners = forms.CharField()
    Funding_requirements = forms.CharField()
    Registered_address = forms.CharField()
    Website = forms.CharField()
    Socia_media_links = forms.CharField()
    founders_email = forms.CharField()
    PAN = forms.CharField()
    Account_No_Bank = forms.CharField()
    Name_of_bank = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
