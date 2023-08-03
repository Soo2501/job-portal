from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from accounts.models import *
from job.models import *
from .models import *
# Create your views here.

def home(request):
    jobs = Job.objects.all()
    paginator =  Paginator(jobs, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    content = {
        "title" : 'Home',
        "page_obj" : page_obj
    }
    return render(request, "home.html", content)

def add_edu(request):
    content = {
        "title" : "profile",
        "page" : "addedu",
        "user": UserProfile.objects.get(user=request.user),
        "edu": Education.objects.filter(user=request.user),
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "cv" : Cv.objects.filter(user=request.user),
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
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "page" : "edit",
        "cv" : Cv.objects.filter(user=request.user),
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

def add_tra(request):
    content = {
        "title" : "profile",
        "page" : "addtrain",
        "user": UserProfile.objects.get(user=request.user),
        "edu": Education.objects.filter(user=request.user),
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "cv" : Cv.objects.filter(user=request.user),
    }
    if request.method == "POST":
        name = request.POST.get("name")
        sdate = request.POST.get("sdate")
        edate = request.POST.get("edate")
        iname = request.POST.get("iname")
        image = request.FILES.get("image")
        edudata = Training.objects.create(name=name,starting_date=sdate, ending_date=edate, institute_name=iname, image=image, user=request.user)
        edudata.save()
        return redirect("profile")
    return render(request,"profile.html",content)

def train_delete(request,id):
    edu = get_object_or_404(Training, id=id, user=request.user)
    edu.delete()
    return redirect("profile")

def add_skills(request):
    content = {
        "title" : "profile",
        "page" : "skills",
        "user": UserProfile.objects.get(user=request.user),
        "edu": Education.objects.filter(user=request.user),
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "cv" : Cv.objects.filter(user=request.user),
    }
    if request.method == "POST":
        skills = request.POST.get("skills")
        edudata = Skills.objects.create(skills=skills, user=request.user)
        edudata.save()
        return redirect("profile")
    return render(request,"profile.html",content)

def add_cv(request):
    content = {
        "title" : "profile",
        "page" : "cv",
        "user": UserProfile.objects.get(user=request.user),
        "edu": Education.objects.filter(user=request.user),
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "cv" : Cv.objects.filter(user=request.user),
    }
    if request.method == "POST":
        image = request.FILES.get("image")
        edudata = Cv.objects.create(image=image, user=request.user)
        edudata.save()
        return redirect("profile")
    return render(request,"profile.html",content)

def edit_cv(request, id):
    cvss = get_object_or_404(Cv, id=id, user=request.user)
    content = {
        "title" : "profile",
        "page" : "cvs",
        "user": UserProfile.objects.get(user=request.user),
        "edu": Education.objects.filter(user=request.user),
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "cv" : Cv.objects.filter(user=request.user)
    }
    if request.method == "POST":
        cvss.image = request.FILES.get("image")
        cvss.save()
        return redirect("profile")
    return render(request, "profile.html", content)

def add_language(request):
    content = {
        "title" : "profile",
        "page" : "language",
        "user": UserProfile.objects.get(user=request.user),
        "edu": Education.objects.filter(user=request.user),
        "train" : Training.objects.filter(user=request.user),
        "skills" : Skills.objects.filter(user=request.user),
        "cv" : Cv.objects.filter(user=request.user),
    }
    if request.method == "POST":
        language = request.POST.get("language")
        edudata = Skills.objects.create(language=language, user=request.user)
        edudata.save()
        return redirect("profile")
    return render(request,"profile.html",content)


def search_data(request):
    title = request.GET['title']
    jtype = request.GET['jtype']
    location = request.GET['location']
    jobs = Job.objects.filter(title__icontains=title , jtype__icontains=jtype, location__icontains=location).values()
    content = {
        "jobs" : jobs,
        "title" : "Search"
    }
    return render(request, "search.html", content)