from django.shortcuts import render,redirect
from schooladmin.models import Schooladmin


# Create your views here.

def home(request):
    return render(request, 'common/home.html')

def aboutus(request):
    return render(request, 'common/about us.html')

def contact(request):
    return render(request, 'common/contact us.html')

def admission(request):
    return render(request, 'common/admission.html')

def master(request):
    return render(request, 'common/master.html')

def adminlogin(request):
    msg=''
    if request.method=='POST':
        username =request.POST['username']
        password = request.POST['password']

        try:
            admin = Schooladmin.objects.get(username = username ,password = password)
            request.session['admin'] = admin.id
            return redirect ('schooladmin:master')
        
        except:
            msg = 'incorrect username or password'
    return render(request, 'common/adminlogin.html',{'message':msg})














