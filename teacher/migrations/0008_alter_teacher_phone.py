# Generated by Django 4.1.5 on 2024-02-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_alter_teacher_age_alter_teacher_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
