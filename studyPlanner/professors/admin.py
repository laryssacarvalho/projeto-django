from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    #list_display = ['name']
    search_fields = ['name']

admin.site.register(Professor, ProfessorAdmin)