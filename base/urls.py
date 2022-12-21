from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('/about', views.aboutPage, name='about-page'),
    path('/contact', views.contactPage, name='contact-page'),
]