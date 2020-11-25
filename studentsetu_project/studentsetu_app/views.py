from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def loginpage(request):
    return render(request, 'login.html')