from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """View to the home page of application"""
    return render(request, 'base/index.html')

def aboutPage(request):
    """View to the about page of application"""
    return render(request, 'base/about.html')

def contactPage(request):
    """View to the contact page of application"""
    return render(request, 'base/contact.html')