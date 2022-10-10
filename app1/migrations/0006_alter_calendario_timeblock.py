# Generated by Django 4.1 on 2022-10-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_course_teacher_calendario_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='timeblock',
            field=models.CharField(choices=[('A', '8:00-8:30'), ('B', '8:30-9:00'), ('C', '9:00-9:30'), ('D', '9:30-10:00'), ('E', '10:00-10:30'), ('F', '10:30-11:00'), ('G', '11:00-11:30'), ('H', '11:30-12:00'), ('I', '13:30-14:00'), ('J', '14:00-14:30'), ('K', '14:30-15:00'), ('L', '15:00-15:30'), ('M', '15:30-16:00'), ('N', '16:00-16:30'), ('O', '16:30-17:00'), ('P', '17:00-17:30'), ('Q', '17:30-18:00'), ('R', '18:00-18:30'), ('S', '18:30-19:00'), ('T', '19:00-19:30'), ('U', '19:30-20:00')], default='A', max_length=10),
        ),
    ]
