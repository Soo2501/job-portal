from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from client.models import *
from django.contrib import messages
# Create your views here.


def user_login(request):
    content = {
        "title" : "Login"
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        
        messages.error(request, "Sorry try again with correct username and password")
        return redirect("login")
    
    return render(request, "login.html", content)


def user_signup(request):
    content = {
        "title" : "Signup"
    }

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create(first_name=firstname,last_name=lastname,username=username,email=email, password=password1)
            user.save()
            return redirect("login")
        
        return redirect("signup")

    return render(request, "signup.html", content)

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required(login_url = "login")
def user_profile(request):
    content = {
        "title" : "profile",
        "user" : UserProfile.objects.get(user=request.user),
        "edu" : Education.objects.filter(user=request.user),
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "paage" : "profile",
        "cv" : Cv.objects.filter(user=request.user)

    }
    return render(request, "profile.html", content)

@login_required(login_url= "login")
def update_profile(request):
    user = UserProfile.objects.get(user=request.user)
    edu = Education.objects.filter(user=request.user)
    train = Training.objects.filter(user=request.user)
    skills = Skills.objects.filter(user=request.user)
    cv = Cv.objects.get(user=request.user)

    if request.method == "POST":
        user.user.first_name = request.POST.get('firstname')
        user.user.last_name = request.POST.get('lastname')
        user.user.username = request.POST.get('username')
        user.user.email = request.POST.get('email')
        profile = request.FILES.get('profile')
        if profile:
            user.profile = profile
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')
        user.phone1 = request.POST.get('phone1')
        birthdate = request.POST.get('birthdate')
        if birthdate:
            user.birthdate = birthdate
        user.save()
        return redirect('profile')
    return render(request, "profile.html" , {"title":"Update Profile","user":user,"page" : "update", "paage":"profile",  "edu":edu, "train":train, "skills":skills })

