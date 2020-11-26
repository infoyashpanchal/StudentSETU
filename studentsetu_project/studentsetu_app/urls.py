from django.urls import path
from . import views

urlpatterns = [
    path('', views.loading_page1, name='loading_page1'),
    
    path('Login_Register', views.loading_page2, name='loading_page2'),
    
    path('Register', views.register_page, name='register_page'),
    path('After_Register', views.after_register, name='after_register'),
    
    path('Login', views.login_page, name='login_page'),
    
    path('Student', views.student_page, name='student_page'),
    
    path('Teacher', views.teacher_page, name='teacher_page'),
]