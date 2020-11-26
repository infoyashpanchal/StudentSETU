from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def loading_page1(request):
    return render(request, 'loading1.html')

def loading_page2(request):
    return render(request, 'loading2.html')

def register_page(request):
    return render(request, 'register.html')

def after_register(request):
    var = True
    return render(request, 'loading2.html', {'var':var})

def login_page(request):
    return render(request, 'login.html')

def student_page(request):
    return render(request, 'student.html')

def teacher_page(request):
    return render(request, 'teacher.html')
