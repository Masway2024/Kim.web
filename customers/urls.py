"""
URL configuration for MaswayApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from customers import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/' , views.about, name='about'),
    path('contact/' , views.contact, name='contact'),
    path('services/' , views.services, name='services'),
    path('portfolio/' , views.portfolio, name='portfolio'),
    path('resume/' ,views.resume, name='resume'),
    path('track_visit', views.track_visit, name='index'),  # Track visits to the homepage
    path('download-cv/', views.download_cv, name='download_cv'),


]
