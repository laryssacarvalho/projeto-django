# Generated by Django 2.0.2 on 2018-03-22 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.User')),
                ('cr', models.FloatField(blank=True, null=True, verbose_name='CR')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
            bases=('core.user',),
        ),
        migrations.CreateModel(
            name='Student_Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeMod1', models.FloatField(verbose_name='Nota Módulo 1')),
                ('gradeMod2', models.FloatField(verbose_name='Nota Módulo 2')),
                ('gradeSub', models.FloatField(verbose_name='Nota Substitutiva')),
                ('idClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Class')),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(blank=True, max_length=255, null=True, verbose_name='Arquivo')),
                ('grade', models.FloatField(verbose_name='Nota')),
                ('hours', models.IntegerField(verbose_name='Horas')),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('idTask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Task')),
            ],
        ),
        migrations.AddField(
            model_name='class_student',
            name='idStudent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]
