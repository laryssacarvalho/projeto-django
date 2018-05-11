from django.db import models
from django.contrib.auth.models import User
from studyPlanner.core.models import Person
from studyPlanner.core.models import Class
from studyPlanner.core.models import Task
from django.dispatch import receiver
from django.db.models.signals import post_save

class Task_Student(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="tasks_students")
    student = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="tasks_students")
    file = models.CharField('Arquivo', max_length=255, null=True, blank=True)
    grade = models.FloatField('Nota')    
    hours = models.IntegerField('Horas')

class Student_Exam(models.Model):
    student = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="students_exams")
    examClass = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="students_exams")
    gradeMod1 = models.FloatField('Nota Módulo 1')
    gradeMod2 = models.FloatField('Nota Módulo 2')
    gradeSub = models.FloatField('Nota Substitutiva')  

    # @receiver(post_save, sender=User)
    # def create_student_exam(sender, instance, created, **kwargs):
    #     if created:
    #         Student_Exam.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_student_exam(sender, instance, **kwargs):
    #     instance.students_exams.save()

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

