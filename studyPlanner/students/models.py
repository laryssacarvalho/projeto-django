from django.db import models
from studyPlanner.core.models import User
from studyPlanner.core.models import Class
from studyPlanner.core.models import Task

class Student(User):
    cr = models.FloatField('CR', null=True, blank=True)
    
    class Meta:
        verbose_name='Aluno'
        verbose_name_plural='Alunos'  

#class Class_Student(models.Model):
#   idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
#  idClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    #notaMod1 = models.FloatField('Nota Módulo 1')
    #notaMod2 = models.FloatField('Nota Módulo 2')
    #notaSub = models.FloatField('Nota Substitutiva')    

class Task_Student(models.Model):
    idTask = models.ForeignKey(Task, on_delete=models.CASCADE)
    idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.CharField('Arquivo', max_length=255, null=True, blank=True)
    grade = models.FloatField('Nota')    
    hours = models.IntegerField('Horas')

class Student_Exam(models.Model):
    idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
    idClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    gradeMod1 = models.FloatField('Nota Módulo 1')
    gradeMod2 = models.FloatField('Nota Módulo 2')
    gradeSub = models.FloatField('Nota Substitutiva')  

