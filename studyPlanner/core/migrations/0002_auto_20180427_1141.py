# Generated by Django 2.0.2 on 2018-04-27 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('professors', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='professors.Professor'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(related_name='classes', to='students.Student'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
