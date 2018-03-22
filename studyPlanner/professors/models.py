from django.db import models
from studyPlanner.core.models import User

# Create your models here.


class Professor(User):
    TIPOS = (
        ('B', 'Bacharel'),        
        ('D', 'Doutor'),
        ('M', 'Mestre')
    )
    graduationType = models.CharField('Graduação', choices=TIPOS, max_length=1)
    class Meta:
        verbose_name='Professor'
        verbose_name_plural='Professores'