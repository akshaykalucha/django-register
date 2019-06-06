from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from  django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserForm, UserProfileInfoForm
# Create your views here.


def login(request):
    return render(request, 'form/login.htm')

def register(request):
    

    registered = False


    if request.method == "POST": 
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True
            return render(request, 'form/base.htm')

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'form/registration.htm', {'user_form':user_form, 'profile_form':profile_form})