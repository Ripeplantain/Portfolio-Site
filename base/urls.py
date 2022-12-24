from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.aboutPage, name='about-page'),
    path('contact/', views.contactPage, name='contact-page'),
    path('login/', views.loginPage, name='login-page'),
    path('register/', views.registerPage, name='register-page'),
    path('logout/', views.logoutUser, name='logout-user'),
    path('downloadpdf/<str:filename>/', views.download_pdf_file, name='download_pdf_file'),
]