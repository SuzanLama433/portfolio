from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def home (request):
    return render(request,'myPortfolio/home.html')

def about(request):
    return render(request,'myPortfolio/about.html')

def skills(request):
    return render(request,'myPortfolio/skills.html')

def project(request):
    searched = request.GET.get("searched")
    if searched:
        data=Project.objects.filter(title__contains=searched)
    else:
        data = Project.objects.all()
    return render(request,'myPortfolio/projects.html',{'data':data})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name,email=email,subject=subject,message=message)
        messages.success(request,f' Hi {name} your message is submited ')
        return redirect('contact')
    return render(request,'myPortfolio/contact.html')