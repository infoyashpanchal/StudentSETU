from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('Register', views.register_page, name='register_page'),
    
    path('Login', views.login_page, name='login_page'),
    
    path('Student', views.student_page, name='student_page'),
    
    path('Teacher', views.teacher_page, name='teacher_page'),
]