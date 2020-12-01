from django.shortcuts import render, redirect
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from django.contrib.auth.models import auth, User


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':

        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('email').split("@")[0]
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if password != re_password:
            messages.error(request, 'Password does not match')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, 'Hurry! You are successfully registered on StudentSETU \t\t Please Login to get started!')
            return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_superuser == 1 :
                return redirect('teacher')
            else:
                return redirect('student')
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def student(request):
    return render(request, 'student.html')

def teacher(request):
    return render(request, 'teacher.html')
