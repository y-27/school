# Generated by Django 4.1.5 on 2024-02-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_alter_teacher_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.BigIntegerField(max_length=10),
        ),
    ]