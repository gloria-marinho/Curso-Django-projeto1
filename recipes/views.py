
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return HttpResponse('HOME')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')

urlpatterns = [
   
    path('admin/',admin.site.urls),
    path('',home),
    path('sobre/', sobre),
    path('contato/',contato),
]