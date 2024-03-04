from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request, 'schooladmin/master.html')

def dashboard(request):
    return render(request, 'schooladmin/dashboard.html')

def fee(request):
    return render(request, 'schooladmin/fee.html')

def notice(request):
    return render(request, 'schooladmin/notice.html')

def studentadmin(request):
    return render(request, 'schooladmin/studentadmin.html')

def teacheradmin(request):
    return render(request, 'schooladmin/teacheradmin.html')

def attendence(request):
    return render(request, 'schooladmin/attendence.html')


