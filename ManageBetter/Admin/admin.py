from django.contrib import admin
from .models import User, Schools, Admin, Student, Teacher, Classes, Grades

# Register your models here.
admin.site.register(Schools)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classes)
admin.site.register(Grades)


