from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from social_django.models import UserSocialAuth



def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'test.html')


