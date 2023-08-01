from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import *
# Create your views here.

def home(request):
    content = {
        "title" : 'Home'
    }
    return render(request, "home.html", content)

def add_edu(request):
    content = {
        "title" : "profile",
        "page" : "addedu",
        "user": UserProfile.objects.get(user=request.user),
        "edu": Education.objects.filter(user=request.user),
    }
    if request.method == "POST":
        name = request.POST.get("name")
        degree = request.POST.get("degree")
        school_name = request.POST.get("school_name")
        date = request.POST.get("date")
        gpa = request.POST.get("gpa")
        image = request.FILES.get("image")
        edudata = Education.objects.create(name=name, degree=degree, school_name=school_name, date=date, gpa=gpa, image=image, user=request.user)
        edudata.save()
        return redirect("profile")
    return render(request,"profile.html",content)

def data_delete(request,id):
    edu = get_object_or_404(Education, id=id, user=request.user)
    edu.delete()
    return redirect("profile")

def edit_data(request, id):
    educ = get_object_or_404(Education, id=id, user=request.user)
    content = {
        "user" : UserProfile.objects.get(user=request.user),
        "edu" : Education.objects.filter(user=request.user),
        "page" : "edit"
    }
    if request.method == "POST":
        educ.name = request.POST.get("name")
        educ.degree = request.POST.get("degree")
        educ.school_name = request.POST.get("school_name")
        educ.date = request.POST.get("date")
        educ.gpa = request.POST.get("gpa")
        image = request.FILES.get("image")
        if image:
            educ.image = image
        educ.save()
        return redirect('profile')
    return render(request,"profile.html", content)