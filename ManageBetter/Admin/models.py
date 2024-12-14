from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Schools Table
class Schools(models.Model):
    schoolid = models.IntegerField(null = False, Default = 1)
    schoolname = models.CharField(max_length=1000, default = '-')

#Admin Table
class Admin(models.Model):
    user = models.OnetoOneField('User', related_name='admins')
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name = "school_admin")

#Students Table
class Student(models.Model):
    user = models.OneToOneField('User', related_name='students')
    grade = models.IntegerField(null = False, Default =1 )
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name = "school_students")

#Teachers Table
class Teacher(models.Model):
    user = models.OneToOneField('User', related_name = 'teachers')
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


    


