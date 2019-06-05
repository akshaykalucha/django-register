from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.


def  base(request):
    return render(request, 'form/base.htm')




def contact(request):
    return render(request, 'form/contact.htm')