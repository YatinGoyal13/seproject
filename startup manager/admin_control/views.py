from django.shortcuts import render
from main.models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def display_data(request):
    user = User.objects.all()
    return render(request, 'adminhome.html', {'user': user})
