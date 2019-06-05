from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from  django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
# Create your views here.


def login(request):
    return render(request, 'form/login.htm')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted Created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request,'form/registration.htm', {'form': form})