# Generated by Django 4.1 on 2022-09-15 12:19

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220909_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='pessoa_imagem',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name=app1.models.upload_image_formater),
        ),
    ]