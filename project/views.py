from django.shortcuts import render, redirect
from project.forms import ProjectForm, CommentForm
from django.contrib import messages
from base.models import Project,Comment
from base.decorators import allowed_users

from django.core.paginator import Paginator

# Create your views here.

def projectPage(request):
    """This is the view to the project page"""
    projects = Project.objects.all()

    paginator = Paginator(projects, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj}
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
            return redirect('project-page')
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

def viewProject(request,pk):
    """View a project"""
    project = Project.objects.get(id=pk)
    comments = Comment.objects.filter(project=project)
    comment_count = Comment.objects.filter(project=project.id).count()

    context = {
                'project':project,
                'comment_count':comment_count,
                'comments':comments,  
                }

    return render(request,'project/view.html',context)

def addComment(request,pk):
    """Add a new comment to the project"""
    form = CommentForm()
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.project_id = pk
            form.save()
            messages.success(request, 'Your comment has been added')
            return redirect('view-project',pk=project.id)

    context = {
                'form': form,
                'project':project,
                }
    return render(request, 'project/add_comment.html', context)

def editComment(request,pk):
    """Edit a comment"""
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    if request.method == 'POST':
        form = ProjectForm(request.POST or None, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('view-project',pk=comment.project.id)

    context = {'form': form}
    return render(request, 'project/add_comment.html',context)

def deleteComment(request,pk):
    """Delete a comment"""
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('view-project',pk=comment.project.id)

    context = {'comment': comment}
    return render(request,'project/delete_comment.html',context)

