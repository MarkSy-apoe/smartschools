from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .models import *
from account.models import *
from .forms import SignUpForm, AccountAuthenticationForm

# Create your views here.
def index(request):
    user = request.user
    context={}

    return render(request, "index.html")

def getstarted(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")

    return render(request, "getstarted.html")

def login(request):
    user = request.user
    context={}

    if user.is_authenticated:
        return redirect("index")
    else:
        if request.POST:
            form = AccountAuthenticationForm(request.POST)
            if form.is_valid():
                
                form.save(request)
                return redirect("index")

            else:
                context['login_form'] = form
    
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("index")
   

def signupCommisioner(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")
    else:
        if request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                CommissionerProfile.objects.create(user=form.save())
                form.save()
                return redirect("login")
            else:
                context['registration_form'] = form

    return render(request, "signupcommisioner.html",context)


def signupDistricthead(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")

    return render(request, "signupdistricthead.html",context)

def signupStatedistrict(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")
    else:
        if request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                StateDistrictHeadProfile.objects.create(user=form.save())
                form.save()
                return redirect("login")
            else:
                context['registration_form'] = form

    return render(request, "signupstatedistrict.html",context)

def signupFeddistrict(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")
    else:
        if request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                FedralDistrictHeadProfile.objects.create(user=form.save())
                form.save()
                return redirect("login")
            else:
                context['registration_form'] = form

    return render(request, "signup_feddistrict.html",context)

