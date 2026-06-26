from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def home (request):
    return render(request,'myPortfolio/home.html')

def about(request):
    context = {
        "journey": Journey.objects.first(),
        "education": Education.objects.all(),
        "skill": Skill.objects.all(),
    }
    return render(request,'myPortfolio/about.html',context)

def skills(request):
    categories = SkillCategory.objects.prefetch_related("skills")
    return render(request,'myPortfolio/skills.html',{'categories':categories})

def project(request):
    searched = request.GET.get("searched")
    if searched:
        data=Project.objects.filter(title__contains=searched)
    else:
        data = Project.objects.all()
    return render(request,'myPortfolio/projects.html',{'data':data})

def contact(request):
    contact_info = MyContact.objects.first()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name,email=email,subject=subject,message=message)
        messages.success(request,f' Hi {name} your message is submited ')
        return redirect('contact')
    return render(request,'myPortfolio/contact.html',{'contact':contact_info})