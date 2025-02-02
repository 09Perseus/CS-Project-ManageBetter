from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#Schools Table
class User(AbstractUser):
    rolechoices = (
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("school_admin", "School Admin"),
    )
    role = models.CharField(max_length=20, choices=rolechoices, default="student")

class Schools(models.Model):
    schoolid = models.IntegerField(null = False, default = 1)
    schoolname = models.CharField(max_length=1000, default = '-')

#Admin Table
class Admin(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='admins')
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name = "school_admin")

#Students Table
class Student(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='students')
    grade = models.IntegerField(null = False, default =1 )
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name = "school_students")

#Teachers Table
class Teacher(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name = 'teachers')
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name = "school_teachers")

#Classes Table
class Classes(models.Model):
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name = "school_classes")
    name = models.CharField(max_length=1000, default = "-")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name = "class_teacher")

#Grades Table
class Grades(models.Model):
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name = "school_grades")
    classid = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name = "classe_grades")
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_grades")
    grades = models.IntegerField(null = False, default = 0)


    


