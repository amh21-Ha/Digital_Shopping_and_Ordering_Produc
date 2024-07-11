# your_app_name/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def register(request):
    return render(request, 'register.html')
