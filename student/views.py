from django.shortcuts import render,redirect
from student.models import Student

# Create your views here.

def studentlogin(request):
    msg = ''
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       student = Student.objects.filter(Email = username,password = password)

       if student.exists():
           request.session['student'] = student[0].id
           return redirect('student:masterstu')
       else:
           msg = 'incorrect password or username '

    #    try:
    #        student = Student.objects.filter(Email = username,password = password)
    #        request.session['student'] = student.id
    #        return redirect('student : masterstu')
        
    #    except:
    #        msg = 'incorrect password or username '

    return render(request, 'student/studentlogin.html',{'message':msg})

def viewattendence(request):
    return render(request, 'student/viewattendence.html')

def masterstu(request):
    return render(request, 'student/masterstu.html')

def studentregister(request):
    msg = ''

    if request.method == 'POST':
        studentName = request.POST['Name']
        studentEmail = request.POST['Email']
        studentAge = request.POST['Age']
        studentgender = request.POST['gender']
        studentphone = request.POST['phone']
        studentaddress = request.POST['address']
        studentpassword = request.POST['password']

        new_student = Student(
            Name = studentName,
            Email = studentEmail,
            Age = studentAge,
            gender = studentgender,
            phone =studentphone,
            address = studentaddress,
            password = studentpassword
        )

        new_student.save()
           
        msg = 'Account Created Succesfully'

    else :
        msg = ''

    return render(request, 'student/studentregister.html',{'message':msg})

def studentdashboard(request):
    return render(request, 'student/studentdashboard.html')




