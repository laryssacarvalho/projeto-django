from django.db import models
#from studyPlanner.students.models import Student

# Create your models here.
class UserManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(name__icontais=query)

class User(models.Model):    
    firstName = models.CharField('Nome', max_length=255, null=False)
    lastName = models.CharField('Sobrenome', max_length=255, null=False)    
    email = models.EmailField('Email',unique=True, null=False)
    ra = models.CharField('RA',max_length=20,null=False, unique=True)
    password = models.CharField('Senha', null=False, max_length=55)
    objects = UserManager()
    def __str__(self):
        return self.firstName
    class Meta:
        verbose_name='Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['firstName','lastName']


class Class(models.Model):
    name = models.CharField('Nome', max_length=255, null=False)
    idProfessor = models.ForeignKey('professors.Professor', on_delete=models.CASCADE)
    idStudent = models.ManyToManyField('students.Student',related_name='Alunos')
    examMod1 = models.DateField('Prova Módulo 1')
    examMod2 = models.DateField('Prova Módulo 2')
    examSub = models.DateField('Prova Substitutiva')
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
    class Meta:
        verbose_name='Tipo de Entrega'         


class Task(models.Model):
    idTaskType = models.ForeignKey(Task_Type, on_delete=models.CASCADE)
    date = models.DateTimeField('Data de Vencimento')
    name = models.CharField('Nome', max_length=255)
    file = models.FileField(upload_to='arquivos', verbose_name='Arquivo', null=True, blank=True)    
    idClass = models.ForeignKey(Class, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Entrega'
        verbose_name_plural = 'Entregas'
        ordering = ['name']
