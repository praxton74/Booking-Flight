"""Flights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.createflight, name="createflight"),
    path('flight/<int:pk>/delete', views.deleteflight, name="deleteflight"),
    path('alltickets/',views.alltickets,name="alltickets"),

    path('', views.home, name="home"),
    path('flights/', views.currentflights, name="currentflights"),
    path('flight/<int:pk>', views.viewflight, name="viewflight"),
    path('flights/(^(?!\s*$).+)',views.searchflights,name="searchflights"), #^(?!\s*$).+
    path('flight/<int:pk>/book', views.bookticket, name="bookticket"),
    path('mytickets/',views.mytickets,name="mytickets"),
    path('ticket/<int:pk>', views.viewticket, name="viewticket"),
    path('ticket/<int:pk>/cancel', views.cancelticket, name="cancelticket"),

    path('signup/', views.signupuser, name="signupuser"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name="loginuser"),



]
