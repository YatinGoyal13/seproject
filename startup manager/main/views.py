from django.shortcuts import render, redirect
from main.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request):
    send_mail(
    'New User Registered',
    'howdy a new user just signed up',
    'forseproject4@gmail.com',
    ['abhay12aps@gmail.com'],
    fail_silently=False,
    )
    return render(request, 'home.html')
def blog(request):
    return render(request, 'blog.html')
def blog_single(request):
    return render(request, 'blog-single.html')



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # error1, error2 = False, False
        print(form.errors)
        if form.is_valid():
            send_mail(
                'New User Registered',
                'howdy a new user just signed up',
                'forseproject4@gmail.com',
                ['abhay12aps@gmail.com'],
            fail_silently=False,
            )
            new_user = form.save(commit=False)
            cd = form.cleaned_data
            new_user.StartUpName = cd['username']
            new_user.save()
            print(str(cd))
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password1'])
            #Write the logic to rerender the page if anyone of the field
            #is not filled.
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('../login/')
                else:
                    messages.error(request,'Disabled account!')
                    form = UserForm()
                    args = {'form': form}
                    return render(request, 'register.html', args)
            else:
                messages.error(request,'Invalid Login')
                form = UserForm()
                args = {'form': form}
                return render(request, 'register.html', args)
        else:
            messages.error(request,'Invalid Form')
            form = UserForm()
            args = {'form': form}
            return render(request, 'register.html', args)
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'register.html', args)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('../startup_profile/')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

@login_required
def startup_profile(request):
    if request.method == 'POST':
        form = UserForm_login(request.POST)
        print (form.errors)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            if user is not None:
                print(user.info_filled)
                if user.info_filled == False:
                    if user.is_active:
                        user.type_of_incorporation = cd['type_of_incorporation']
                        user.name_of_legal_entity = cd['name_of_legal_entity']
                        user.Directors_Partners = cd['Directors_Partners']
                        user.Funding_requirements = cd['Funding_requirements']
                        user.Registered_address = cd['Registered_address']
                        user.Website = cd['Website']
                        user.Socia_media_links = cd['Socia_media_links']
                        user.founders_email = cd['founders_email']
                        user.PAN = cd['PAN']
                        user.Account_No_Bank = cd['Account_No_Bank']
                        user.Name_of_bank = cd['Name_of_bank']
                        user.info_filled = True
                        user.save()
                        login(request, user)
                        # return HttpResponse('Done')
                        return redirect('../startup_profile/profile')
                        #To add the next routing here.
                    else:
                        return HttpResponse('Disabled account')
                else:
                    # return HttpResponse('Done')
                    return redirect('../startup_profile/profile')
            else:
                return HttpResponse('Invalid Login')
    else:
        user = request.user
        if user.info_filled == False:
            form = UserForm_login()
            return render(request, 'reg_form_login.html', {'form': form})
        else:
            # return HttpResponse('Done')
            #To add the next routing here.
            return redirect('../startup_profile/profile')

@login_required
def startup_profile_pro(request):
    user = request.user
    if user is not None:
        if user.is_active:
            login(request, user)
            student = request.user
            return render(request, 'profile.html', {'user': user})
        else:
            return HttpResponse('Disabled account')
    else:
        return HttpResponse('Invalid Login')

def logout_view(request):
    logout(request)
    return redirect('/')
