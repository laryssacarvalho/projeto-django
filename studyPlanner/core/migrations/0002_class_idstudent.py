# Generated by Django 2.0.2 on 2018-03-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='idStudent',
            field=models.ManyToManyField(related_name='Alunos', to='students.Student'),
        ),
    ]
