from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('project/', views.projectPage, name='project-page'),
    path('create/', views.createProject, name='create-project'),
    path('update/<str:pk>/', views.updateProject, name='update-project'),
    path('delete/<str:pk>/', views.deleteProject, name='delete-project'),
]