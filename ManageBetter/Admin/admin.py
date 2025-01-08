from django.contrib import admin
from .models import User, Schools, Admin, Student, Teacher, Classes, Grades
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(DefaultUserAdmin):
    # Add 'role' to list_display for easier viewing
    list_display = ("username", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")

    # Add 'role' to fieldsets for editing in the admin
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal Info"), {"fields": ("role", "first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Add 'role' to the add_fieldsets for creating users
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "role"),
        }),
    )

    # Search by email and role
    search_fields = ("username", "role")
    ordering = ("username",)


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Schools)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classes)
admin.site.register(Grades)


