from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstName','lastName','ra','email']
    search_fields = ['firstName', 'lastName', 'ra', 'email']

admin.site.register(Student, StudentAdmin)


