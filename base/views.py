from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user

import mimetypes
import os
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    """View to the home page of application"""
    return render(request, 'base/index.html')

def download_pdf_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/images/images/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'base/index.html')

def aboutPage(request):
    """View to the about page of application"""
    return render(request, 'base/about.html')

def contactPage(request):
    """View to the contact page of application"""
    return render(request, 'base/contact.html')

@unauthenticated_user
def loginPage(request):
    """View to the login page of application"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'You have logged in successfully')
            return redirect('home')
        else:
            messages.info(request, 'username or password incorrect')

    context = {}
    return render(request, 'base/login.html', context)

@unauthenticated_user
def registerPage(request):
    """View to register page of application"""
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = request.POST.get('password1')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'You have logged in successfully')
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/register.html', context)

def logoutUser(request):
    """Logout the user"""
    logout(request)
    return redirect('login-page')