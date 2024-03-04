from django.db import models

# Create your models here.


class Student (models.Model) :
    Name = models.CharField(max_length = 30,default='')
    address = models.CharField(max_length = 200,default='')
    Email = models.CharField(max_length = 30, default='')
    gender = models.CharField(max_length = 30,default='')
    phone = models.BigIntegerField() 
    Age = models.CharField(max_length=10)
    password = models.CharField(max_length=20,default='')

    class Meta :
        db_table = 'student_tb'























































