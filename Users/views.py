from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *

def register(request):
    if request.method  == 'POST':
        form  = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)



