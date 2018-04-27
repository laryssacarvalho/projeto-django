from django.contrib import admin
from .models import Class
from .models import Task
from .models import Task_Type
from .models import User
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Class, ClassAdmin)
admin.site.register(Task)
admin.site.register(Task_Type)
admin.site.register(User)
