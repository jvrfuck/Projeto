# Generated by Django 4.1 on 2022-10-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_pessoas_pessoa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='timeblock',
            field=models.CharField(choices=[('A', '8:00-8:20'), ('B', '8:20-8:40'), ('C', '8:40-9:00'), ('D', '9:00-9:20'), ('E', '9:20-9:40'), ('F', '9:40-10:00'), ('G', '10:00-10:20'), ('H', '10:40-11:00'), ('I', '11:00-11:20'), ('J', '11:20-11:40'), ('K', '11:40-12:00'), ('L', '13:30-13:50'), ('M', '14:00-14:20'), ('N', '14:20-14:40'), ('O', '15:00-15:20'), ('P', '15:20-15:40'), ('Q', '15:40-16:00'), ('R', '16:00-16:20'), ('S', '16:20-16:40'), ('T', '16:40-17:00'), ('U', '17:00-17:20'), ('V', '17:20-17:40'), ('W', '17:40-18:00'), ('X', '18:00-18:20'), ('Y', '18:20-18:40'), ('Z', '18:40-19:00')], default='A', max_length=10),
        ),
    ]