from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email',unique=True)
    ra = models.CharField('RA',max_length=20,null=False, unique=True)
    idade = model.IntegerField('Idade')