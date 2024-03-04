from django.urls import path
from . import views

app_name='teacher'

urlpatterns = [
    path('teacherlogin', views.teacherlogin,name='teacherlogin'),
    path('teachersignup', views.teachersignup,name='teachersignup'),
    path('master', views.master,name='master'),

     
     
     
]
