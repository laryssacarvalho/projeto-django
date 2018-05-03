from django.db import models
from studyPlanner.core.models import Person
from studyPlanner.core.models import Class
from studyPlanner.core.models import Task

class Student(Person):
    cr = models.FloatField('CR', null=True, blank=True)
    
    class Meta:
        verbose_name='Aluno'
        verbose_name_plural='Alunos'  

class Task_Student(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="tasks_students")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="tasks_students")
    file = models.CharField('Arquivo', max_length=255, null=True, blank=True)
    grade = models.FloatField('Nota')    
    hours = models.IntegerField('Horas')

class Student_Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="students_exams")
    examClass = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="students_exams")
    gradeMod1 = models.FloatField('Nota Módulo 1')
    gradeMod2 = models.FloatField('Nota Módulo 2')
    gradeSub = models.FloatField('Nota Substitutiva')  

