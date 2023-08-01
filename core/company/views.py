from django.shortcuts import render

# Create your views here.
def home(request):
    content = {
        "title" : "home"
    }
    return render(request,"home.html", content)