from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request,'myPortfolio/home.html')

def about(request):
    return render(request,'myPortfolio/about.html')

def skills(request):
    return render(request,'myPortfolio/skills.html')

def project(request):
    return render(request,'myPortfolio/projects.html')

def contact(request):
    return render(request,'myPortfolio/contact.html')