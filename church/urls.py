"""church URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from churchApp import views
urlpatterns = [
    path('contentcontrol/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('pastoraCorner/',views.pastora_corner,name='pastora_corner'),
    path('pastoraCorner/list',views.sermon_list,name='sermon_list'),
    path('pastoraCorner/list/(?P<urlId>\d+)',views.sermon_list_prev,name='sermon_list_prev'),
    path('app/',views.SPA,name='SPA'),
    path('mapp/',views.mobileSPA,name='mobileSPA'),
]
