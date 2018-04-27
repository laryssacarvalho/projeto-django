from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)

class User(AbstractBaseUser, PermissionsMixin):    
    firstName = models.CharField('Nome', max_length=255, null=False)
    lastName = models.CharField('Sobrenome', max_length=255, null=False)    
    username = models.CharField('Usuário', max_length=30, unique=True)
    email = models.EmailField('Email',unique=True, null=False)
    ra = models.CharField('RA',max_length=20,null=False, unique=True)
    password = models.CharField('Senha', null=False, max_length=55)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.firstName

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)
        
    class Meta:
        verbose_name='Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['firstName','lastName']


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
    professor = models.ForeignKey('professors.Professor', on_delete=models.CASCADE, related_name="classes")
    students = models.ManyToManyField('students.Student',related_name='classes')
    examMod1 = models.DateField('Prova Módulo 1')
    examMod2 = models.DateField('Prova Módulo 2')
    examSub = models.DateField('Prova Substitutiva')
    code = models.CharField('Código', max_length=45, null=False, blank=True)
    room = models.CharField('Sala', max_length=20, null=False, blank=True)    
    weekDay = models.CharField('Dia da Semana', max_length=20, choices=SEMANA, default='SEGUNDA')
    horario = models.TimeField('Horário', default='', blank=True)

    def __str__(self):
        return self.name
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
