# Generated by Django 4.1 on 2022-09-23 14:21

import app1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CalendarioCreated', models.DateTimeField(auto_now_add=True, verbose_name='TimeStamp')),
            ],
            options={
                'verbose_name': 'calendario',
                'verbose_name_plural': 'calendarios',
                'ordering': (),
            },
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horarioCreated', models.DateTimeField(auto_now_add=True, verbose_name='TimeStamp')),
                ('ativo', models.CharField(default='S', max_length=1)),
                ('horario_empresa', models.CharField(default=None, max_length=100, verbose_name='Horario da empresa')),
                ('horario_pessoas', models.CharField(default=None, max_length=100, verbose_name='Horario Pessoa')),
                ('horario_local', models.CharField(default=None, max_length=100, verbose_name='Horario Local')),
                ('horario_servico', models.CharField(default=None, max_length=100, verbose_name='Horario Servico')),
                ('horario_duracao', models.DateField(default=None, max_length=100, verbose_name='horario duracao')),
                ('horario_inicio', models.DateField(default=None, max_length=100, verbose_name='horario inicio')),
                ('horario_tipo', models.CharField(default=None, max_length=100, verbose_name='horario tipo')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
                'ordering': ('horario_servico', 'horario_empresa', 'horario_pessoas'),
            },
        ),
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localCreated', models.DateTimeField(auto_now_add=True, verbose_name='TimeStamp')),
                ('ativo', models.CharField(default=None, max_length=1)),
                ('local_nome', models.CharField(default=None, max_length=100, verbose_name='Nome do Local')),
                ('local_endereco', models.CharField(default=None, max_length=100, verbose_name='Endereco do Local')),
                ('local_descricao', models.CharField(default=None, max_length=100, verbose_name='Descricao do Local')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locais',
                'ordering': ('local_nome', 'local_endereco', 'local_descricao'),
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa_created', models.DateTimeField(auto_now_add=True, verbose_name='TimeStamp')),
                ('ativo', models.CharField(default='S', max_length=1)),
                ('pessoa_nome', models.CharField(default=None, max_length=100, verbose_name='Nome da Pessoa')),
                ('pessoa_telefone', models.CharField(default=None, max_length=100, verbose_name='Telefone da Pessoa')),
                ('pessoa_endereco', models.CharField(default=None, max_length=100, verbose_name='Endereco da Pessoa')),
                ('pessoa_email', models.CharField(default=None, max_length=100, verbose_name='Email da Pessoa')),
                ('pessoa_imagem', models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name=app1.models.upload_image_formater)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ('pessoa_nome', 'pessoa_endereco'),
            },
        ),
        migrations.CreateModel(
            name='Pessoas_Fisicas',
            fields=[
                ('pessoas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.pessoas')),
                ('pf_cpf', models.CharField(default=None, max_length=100, verbose_name='CPF da Pessoa')),
                ('pf_datanascimento', models.DateField(default=None, max_length=100, verbose_name='Data de Nascimento')),
                ('pf_fidelidade', models.CharField(default=None, max_length=100, verbose_name='Fidelidade da Pessoa')),
            ],
            options={
                'verbose_name': 'Pessoa_Fisica',
                'verbose_name_plural': 'Pessoas_Fisicas',
                'ordering': ('pf_cpf', 'pf_datanascimento'),
            },
            bases=('app1.pessoas',),
        ),
        migrations.CreateModel(
            name='Pessoas_Juridicas',
            fields=[
                ('pessoas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.pessoas')),
                ('pj_atividade', models.CharField(default=None, max_length=100, verbose_name='Atividades da empresa')),
                ('pj_cnpj', models.CharField(default=None, max_length=100, verbose_name='CNPJ da empresa')),
                ('pj_servico', models.CharField(default=None, max_length=100, verbose_name='Servico da empresa')),
            ],
            options={
                'verbose_name': 'Pessoas_Juridica',
                'verbose_name_plural': 'Pessoas_Juridicas',
                'ordering': ('pj_atividade',),
            },
            bases=('app1.pessoas',),
        ),
    ]
