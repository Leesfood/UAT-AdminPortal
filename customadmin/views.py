# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Make sure 'home.html' exists in your templates
