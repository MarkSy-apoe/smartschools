from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .models import *
from account.models import *
from .forms import SignUpForm, AccountAuthenticationForm, SchoolForm

# Create your views here.
def index(request):
    user = request.user
    posts = Post.objects.all()
    
    context={
        'posts': posts,
    }

    if user.is_authenticated:
        getposts = Post.objects.filter(user=user)[:5] 
        context['yourpost'] = getposts
        if user.accounttype == 'ministerOE':
            profile = MinisterProfile.objects.get(user=user)          
            context['profile'] = profile
        elif user.accounttype == 'commissioner':
            profile = CommissionerProfile.objects.get(user=user)
            context['profile'] = profile
        elif user.accounttype == 'fedraldistrict':
            profile = FedralDistrictHeadProfile.objects.get(user=user)
            context['profile'] = profile
        elif user.accounttype == 'statedistrict':
            profile = StateDistrictHeadProfile.objects.get(user=user)
            context['profile'] = profile
        elif user.accounttype == 'principal':
            profile = PrincipalProfile.objects.get(user=user)
            context['profile'] = profile
            if profile.school:
                school = profile.school
                context["school"] = school
        elif user.accounttype == 'student':
            profile = StudentProfile.objects.get(user=user)
            context['profile'] = profile
            if profile.school:
                school = profile.school
                context["school"] = school
        elif user.accounttype == 'teacher':
            profile = TeacherProfile.objects.get(user=user)
            context['profile'] = profile
            if profile.school:
                school = profile.school
                context["school"] = school
        else:
            pass

    return render(request, "index.html", context)

def getstarted(request):
    user = request.user

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
                CommissionerProfile.objects.create(state=request.POST.get("state"), user=form.save())
                form.save()
                return redirect("login")
            else:
                context['registration_form'] = form

    return render(request, "signupcommisioner.html",context)


def principalsignup(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")
    else:
        if request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                PrincipalProfile.objects.create(user=form.save())
                form.save()
                return redirect("login")
            else:
                context['registration_form'] = form

    return render(request, "principalsignup.html",context)


def studentsignup(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")
    else:
        if request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                StudentProfile.objects.create(user=form.save())
                form.save()
                return redirect("login")
            else:
                context['registration_form'] = form

    return render(request, "studentsignup.html",context)

def teachersignup(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        return redirect("index")
    else:
        if request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                TeacherProfile.objects.create(user=form.save())
                form.save()
                return redirect("login")
            else:
                context['registration_form'] = form

    return render(request, "teachersignup.html",context)


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

    return render(request, "signup_feddistrict.html", context)

def createschool(request):
    user = request.user
    context={}

    if user.accounttype == 'principal':
        profile = PrincipalProfile.objects.get(user=user)
        if profile.school:
            return redirect("school")
        

    if user.is_authenticated == False:
        return redirect("index")
    else:
        if request.POST:
            form = SchoolForm(request.POST)
            if form.is_valid():
                if user.accounttype == 'principal':
                    profile = PrincipalProfile.objects.get(user=user)
                    profile.school = form.save()
                    profile.save()
                    return redirect("school")
                else:
                    School.objects.create(form.save())
                    return redirect("school")
            else:
                context['schoolform'] = form

    return render(request, "createschool.html", context)

def schoolprofile(request, pk):
    user = request.user
    school = School.objects.get(slug=pk)

    context = {
        'school': school,
    }

    return render(request, "schoolprofile.html", context)


def createpost(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        if request.POST:
            post = Post(user=user, content=request.POST.get("content"))
            post.save()
            return redirect("index")
    else:
        return redirect("index")
    
    return render(request, "createpost.html", context)


def managecommissioner(request):
    user = request.user
    context ={}

    if user.is_authenticated:
        if user.accounttype == 'ministerOE':
            commissioners = Account.objects.filter(is_confirmed=False)
            context["toapprove"] = commissioners
        else:
            return redirect("index")
    else:
        return redirect("index")
    
    return render(request, "manage_comm.html", context)
