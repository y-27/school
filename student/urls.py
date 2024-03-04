from django.urls import path
from . import views

app_name='student'


urlpatterns = [
    path('studentlogin', views.studentlogin,name='studentlogin'),
    path('viewattendence', views.viewattendence,name='viewattendence'),
    path('masterstu', views.masterstu,name='masterstu'),
    path('studentregister', views.studentregister,name='studentregister'),
    path('studentdashboard', views.studentdashboard,name='studentdashboard'),
    
    
]
