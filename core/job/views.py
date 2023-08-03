from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *
from accounts.models import *
# Create your views here.


@login_required(login_url="login")
def job_form(request):
    content = {
        "title" : "Add Job"
    }
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        jtype = request.POST.get('jtype')
        description = request.POST.get('description')
        requirements = request.POST.get('requirements')
        wsite = request.POST.get('wsite')
        deadline = request.POST.get('deadline')
        job = Job.objects.create(title=title, company=company, location=location, jtype=jtype, desc=description, requirements=requirements, wsite=wsite, deadline=deadline, user=request.user)
        job.save()
        return redirect("home")
    return render(request,"jobs.html", content)


def category(request):
    content = {
        "title" : "Category",
        "jobs" : Job.objects.all()
    }
    return render(request, "category.html", content)


def job_detail(request,id):
    content={
        "title" : "Detail page",
        "job" : Job.objects.get(id=id)
    }
    return render(request, "job-detail.html", content)

@login_required(login_url="login")
def job_apply(request,id):
    job = Job.objects.get(id=id)
    profile = UserProfile.objects.get(user=request.user)
    content = {
        "title" : "apply",
        "job" : job,
        "profile": profile
    }
    if  job.user == request.user:
        messages.error(request,"Sorry you cannot apply your own job")
        return redirect("home")
    return render(request, "job-apply.html", content)
    