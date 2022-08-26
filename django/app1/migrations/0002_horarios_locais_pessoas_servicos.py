# Generated by Django 4.1 on 2022-08-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_empresa', models.CharField(blank=True, max_length=200, verbose_name='Empresa')),
                ('horario_pessoas', models.CharField(blank=True, max_length=200, verbose_name='Pessoa')),
                ('horario_local', models.CharField(blank=True, max_length=200, verbose_name='Local')),
                ('horario_servico', models.CharField(blank=True, max_length=200, verbose_name='Serviço')),
                ('horario_duracao', models.CharField(blank=True, max_length=200, verbose_name='Duração')),
                ('horario_inicio', models.CharField(blank=True, max_length=200, verbose_name='Início')),
                ('horario_tipo', models.CharField(blank=True, max_length=200, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_nome', models.CharField(blank=True, max_length=200, verbose_name='Nome')),
                ('local_endereco', models.CharField(blank=True, max_length=200, verbose_name='Endereço')),
                ('local_descricao', models.CharField(blank=True, max_length=200, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa_nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('pessoa_cpf', models.CharField(blank=True, max_length=100, verbose_name='CPF')),
                ('pessoa_nascimento', models.DateField(blank=True, max_length=20, verbose_name='Data de nascimento')),
                ('pessoa_telefone', models.CharField(blank=True, max_length=200, verbose_name='Telefone')),
                ('pessoa_email', models.CharField(blank=True, max_length=200, verbose_name='E-mail')),
                ('pessoa_fidelidade', models.CharField(blank=True, max_length=200, verbose_name='Fidelidade')),
            ],
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico_nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('servico_registroClasse', models.CharField(blank=True, max_length=100, verbose_name='registroClasse')),
                ('servico_descricao', models.CharField(blank=True, max_length=100, verbose_name='descricao')),
                ('servico_miniCV', models.CharField(blank=True, max_length=200, verbose_name='miniCV')),
                ('servico_valor', models.FloatField(blank=True, max_length=50, verbose_name='valor')),
            ],
        ),
    ]