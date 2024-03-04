from django.urls import path
from . import views

app_name='schooladmin'

urlpatterns = [
     path('master', views.master,name='master'),
     path('dashboard', views.dashboard,name='dashboard'),
     path('attendence', views.attendence,name='attendence'),
     path('fee', views.fee,name='fee'),
     path('notice', views.notice,name='notice'),
     path('studentadmin', views.studentadmin,name='studentadmin'),
     path('teacheradmin', views.teacheradmin,name='teacheradmin'),
     
]