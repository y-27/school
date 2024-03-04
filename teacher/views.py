from django.shortcuts import render,redirect

from teacher.models import Teacher

# Create your views here.


def teacherlogin(request):
    msg = ''

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        try :
            teacher = Teacher.objects.get(username = username, password = password)
            request.session['teacher']=teacher[0].id
            return redirect('teacher:teachersignup')
        
        except :
            msg = 'incorrect username or password '
    return render(request, 'teacher/teacherlogin.html',{'message':msg})

def teachersignup(request):
    msg = ''

    if request.method == 'POST':
        Tname = request.POST['name']
        Temail = request.POST['email']
        Tpassword = request.POST['password']

        new_teacher = Teacher(
            name = Tname,
            email = Temail,
            password = Tpassword
        )
        new_teacher.save()
           
        msg = 'Account Created Succesfully'

    else :
        msg = ''
    
    return render(request, 'teacher/teachersignup.html',{'message':msg})

def master(request):
    return render(request, 'teacher/master.html')

