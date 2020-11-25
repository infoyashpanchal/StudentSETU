from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def function1(request):
    return render(request, 'index.html')