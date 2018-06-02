from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Person(models.Model):
    TIPO = (
        ('S', 'Aluno'),
        ('P', 'Professor')        
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ra = models.CharField('RA',max_length=20,null=False)    
    tipo = models.CharField('Tipo de Usuário', max_length=10, choices=TIPO, default='S')    
    
    def __str__(self):
        return (self.user.first_name + ' ' + self.user.last_name + ' - ' + str(self.user.person.ra))

    def get_full_name(self):
        return str(self)
    
    @receiver(post_save, sender=User)
    def create_user_person(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_person(sender, instance, **kwargs):
        instance.person.save()

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

class Class(models.Model):
    SEMANA = (
        ('SEGUNDA', 'Segunda-Feira'),
        ('TERCA', 'Terça-Feira'),
        ('QUARTA', 'Quarta-Feira'),
        ('QUINTA', 'Quinta-Feira'),
        ('SEXTA', 'Sexta-Feira'),
        ('SABADO', 'Sábado')
    )
    name = models.CharField('Nome', max_length=255, null=False)
    professor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="classes_professor")
    students = models.ManyToManyField(Person,related_name='classes_student')
    examMod1 = models.DateField('Prova Módulo 1')
    examMod2 = models.DateField('Prova Módulo 2')
    examSub = models.DateField('Prova Substitutiva')
    code = models.CharField('Código', max_length=45, null=False, blank=True)
    room = models.CharField('Sala', max_length=20, null=False, blank=True)    
    weekDay = models.CharField('Dia da Semana', max_length=20, choices=SEMANA, default='SEGUNDA')
    horario = models.TimeField('Horário', default='', blank=True)

    def __str__(self):
        return (self.code + ' - ' + self.name)
    class Meta:
        verbose_name='Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['name']

class Task_Type(models.Model):
    TIPOS = (
        ('P', 'Pessoal'),
        ('F', 'Faculdade'),
    )
    name = models.CharField('Nome', max_length=255)
    type = models.CharField('Tipo', max_length=1, choices=TIPOS)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Tipo de Entrega'         


class Task(models.Model):
    idTaskType = models.ForeignKey(Task_Type, on_delete=models.CASCADE)
    date = models.DateTimeField('Data de Vencimento')
    name = models.CharField('Nome', max_length=255)
    file = models.FileField(upload_to='arquivos', verbose_name='Arquivo', null=True, blank=True)    
    taskClass = models.ForeignKey(Class, null=False, on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Entrega'
        verbose_name_plural = 'Entregas'
        ordering = ['name']
