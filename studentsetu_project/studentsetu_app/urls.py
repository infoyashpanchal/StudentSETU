from django.urls import path
from . import views

urlpatterns = [
    path('',views.function1,name='function1')
]