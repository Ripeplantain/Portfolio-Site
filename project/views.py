from django.shortcuts import render, redirect
from project.forms import ProjectForm
from django.contrib import messages
from base.models import Project
from base.decorators import allowed_users

# Create your views here.

def projectPage(request):
    """This is the view to the project page"""
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project/project.html', context)

@allowed_users(allowed_roles=['admin'])
def createProject(request):
    """This is the view to the create project"""
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Post has been created successfully')
            return redirect('home')
    context = {'form': form}
    return render(request, 'project/create.html', context)

@allowed_users(allowed_roles=['admin'])
def updateProject(request, pk):
    """This is the view for updating a project"""
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-page')
    context = {'form': form}
    return render(request,'project/create.html',context)

@allowed_users(allowed_roles=['admin'])
def deleteProject(request,pk):
    """Delete a project"""
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project-page')

    context = {'project': project}
    return render(request,'project/delete.html',context)

