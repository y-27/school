# Generated by Django 4.1.5 on 2024-02-20 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0012_alter_teacher_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='age',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone',
        ),
    ]
