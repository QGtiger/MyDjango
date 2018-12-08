from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def loginView(request):
    title = ' '