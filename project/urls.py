from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('project/', views.projectPage, name='project-page'),
    path('create/', views.createProject, name='create-project'),
    path('update/<str:pk>/', views.updateProject, name='update-project'),
    path('delete/<str:pk>/', views.deleteProject, name='delete-project'),
    path('view/<str:pk>/', views.viewProject, name='view-project'),
    path('comment/<str:pk>', views.addComment, name='add-comment'),
    path('delete_comment/<str:pk>/', views.deleteComment, name='delete-comment'),
    path('edit_comment/<str:pk>/', views.editComment, name='edit-comment'),
]