from django.contrib import admin
from .models import Class

# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Class, ClassAdmin)