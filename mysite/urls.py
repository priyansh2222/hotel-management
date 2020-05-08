"""
Definition of urls for mysite.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('ourhotel/', views.ourhotel, name='ourhotel'),
    path('reg/',views.reg,name='reg'),
   
    path('yourorder',views.yourorder,name='yourorder'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('contact/', views.contact, name='contact'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('bc',views.bc,name='bc'),
    path('bms/', views.bms, name='bms'),
    
   
    path('admin/', admin.site.urls)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 