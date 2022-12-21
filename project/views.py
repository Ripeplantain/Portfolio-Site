from django.shortcuts import render
from project.forms import ProjectForm

# Create your views here.

def projectPage(request):
    """This is the view to the project page"""
    context = {}
    return render(request, 'project/project.html', context)

def createProject(request):
    """This is the view to the create project"""
    form = ProjectForm()
    context = {'form':form}
    return render(request, 'project/create.html', context)