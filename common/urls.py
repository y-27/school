from django.urls import path
from . import views

app_name='common'

urlpatterns = [
     path('home', views.home,name='home'),
     path('aboutus', views.aboutus,name='aboutus'),
     path('contact', views.contact,name='contact'),
     path('admission', views.admission,name='admission'),
     path('master', views.master,name='master'),
     path('adminlogin', views.adminlogin,name='adminlogin'),
     
]                                                                                                                                                               