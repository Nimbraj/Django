"""
URL configuration for sbi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from carloan import urls as cc
from upi import urls as up
from balance import urls as bal
from insurance import urls as ins





urlpatterns = [
    path("admin/", admin.site.urls),
    path('mains/',include(cc))  
    path('mains/',include(bal))  
    path('mains/',include(ins))  
    
    
]
