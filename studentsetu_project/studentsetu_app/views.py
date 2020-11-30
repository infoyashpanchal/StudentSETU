from operator import itemgetter
import mysql.connector
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, reverse

from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register_page(request):
    if request.method == 'POST':
        user = User()
        user.fname = request.POST.get('fname')
        user.lname = request.POST.get('lname')
        user.gender = request.POST.get('gender')
        user.department = request.POST.get('department')
        user.Class = request.POST.get('Class')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.re_password = request.POST.get('re_password')

        if user.password != user.re_password:
            messages.info(request, 'Password does not match')
            return redirect('register_page')
        else:
            user.save()
            messages.success(request, 'Hurry! You are successfully reistered on StudentSETU')
            return redirect('register_page')
    return render(request, 'register.html')

def login_page(request):
    con = mysql.connector.connect(host = '127.0.0.1', user = 'yash', password = 'yash123', database = 'studentsetu')
    cursor = con.cursor()
    con2 = mysql.connector.connect(host = '127.0.0.1', user = 'yash', password = 'yash123', database = 'studentsetu')
    cursor2 = con2.cursor()
    con3 = mysql.connector.connect(host = '127.0.0.1', user = 'yash', password = 'yash123', database = 'studentsetu')
    cursor3 = con3.cursor()
    sql = "select email from studentsetu_app_user;"
    sql2 = "select password from studentsetu_app_user;"
    sql3 = "select fname from studentsetu_app_user;"
    cursor.execute(sql)
    cursor2.execute(sql2)
    cursor3.execute(sql3)

    e = []
    p = []
    n = []
    for i in cursor:
        e.append(i)
    for i in cursor2:
        p.append(i)
    for i in cursor3:
        n.append(i)
    
    
    email_list = list(map(itemgetter(0), e))
    password_list = list(map(itemgetter(0), p))
    name_list = list(map(itemgetter(0), n))
    
    if request == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        i = 0
        k = len(email_list)
        for i in range(k):
            if email_list[i] == email and password_list[i] == password:
                name = name_list[i]
                return render(request, 'student.html', {'name':name})
                break
            i += 1
        else:
            messages.info(request, 'invalid Email or Passowrd!')
            return redirect('login_page')
    return render(request, 'login.html')

def student_page(request):
    return render(request, 'student.html')

def teacher_page(request):
    return render(request, 'teacher.html')
