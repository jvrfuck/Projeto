from django.db import models

# Create your models here.

class Empresas (models.Model):
    empresa_nome = models.CharField(max_length=200,verbose_name="Nome", blank=True)
    empresa_atividade = models.CharField(max_length=200,verbose_name="Atividade", blank=True)
    empresa_cnpj = models.CharField(max_length=200,verbose_name="CNPJ", blank=True)
    empresa_endereco = models.CharField(max_length=200,verbose_name="Endereço", blank=True)
    empresa_telefone = models.CharField(max_length=200,verbose_name="Telefone", blank=True)
    empresa_email = models.CharField(max_length=200,verbose_name="E-mail", blank=True)
    empresa_servico = models.CharField(max_length=200,verbose_name="Serviço", blank=True)


class Pessoas (models.Model):
    pessoa_nome = models.CharField(max_length=100,verbose_name="Nome", blank=True)
    pessoa_cpf = models.CharField(max_length=100,verbose_name="CPF", blank=True)
    pessoa_nascimento = models.DateField(max_length=20,verbose_name="Data de nascimento", blank=True)
    pessoa_telefone = models.CharField(max_length=200,verbose_name="Telefone", blank=True)
    pessoa_email = models.CharField(max_length=200,verbose_name="E-mail", blank=True)
    pessoa_fidelidade = models.CharField (max_length=200,verbose_name="Fidelidade", blank=True)


class Locais (models.Model):
    local_nome = models.CharField(max_length=200,verbose_name="Nome", blank=True)
    local_endereco = models.CharField(max_length=200,verbose_name="Endereço", blank=True)
    local_descricao = models.CharField(max_length=200,verbose_name="Descrição", blank=True)


class Servicos (models.Model):
    servico_nome = models.CharField(max_length=100, blank=True, verbose_name='Nome')
    servico_registroClasse = models.CharField(max_length=100, blank=True, verbose_name='registroClasse')
    servico_descricao = models.CharField(max_length=100, blank=True, verbose_name='descricao')
    servico_miniCV = models.CharField(max_length=200, blank=True, verbose_name='miniCV')
    servico_valor = models.FloatField(max_length=50, blank=True, verbose_name='valor')


class Horarios(models.Model):
	horario_empresa = models.CharField(max_length=200,verbose_name="Empresa", blank=True)
	horario_pessoas = models.CharField(max_length=200,verbose_name="Pessoa", blank=True)
	horario_local = models.CharField(max_length=200,verbose_name="Local", blank=True)
	horario_servico = models.CharField(max_length=200,verbose_name="Serviço", blank=True)
	horario_duracao = models.CharField(max_length=200,verbose_name="Duração", blank=True)
	horario_inicio = models.CharField(max_length=200,verbose_name="Início", blank=True)
	horario_tipo = models.CharField(max_length=200,verbose_name="Tipo", blank=True)
