from django.shortcuts import render
from .models import *

# Create your views here.

def home (request):
    return render(request,'myPortfolio/home.html')

def about(request):
    return render(request,'myPortfolio/about.html')

def skills(request):
    return render(request,'myPortfolio/skills.html')

def project(request):
    data = Project.objects.all()
    return render(request,'myPortfolio/projects.html',{'data':data})

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
    return render(request,'myPortfolio/contact.html')