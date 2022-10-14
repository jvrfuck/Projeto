from django.db import models
import uuid
from django.utils import timezone
from django.urls import reverse
from datetime import date
from allauth import app_settings as allauth_app_settings
# Create your models here.

def upload_image_formater(instance, filename):
    return f"{str(uuid.uuid4())}.{filename})"


class Pessoas(models.Model):
    pessoa_created = models.DateTimeField(verbose_name="TimeStamp", auto_now_add=True)
    ativo = models.CharField(max_length =1,default="S")
    pessoa_nome = models.CharField(max_length = 100,verbose_name="Nome da Pessoa",default=None)
    pessoa_telefone = models.CharField(max_length = 100,verbose_name="Telefone da Pessoa",default=None)
    pessoa_endereco = models.CharField(max_length = 100,verbose_name="Endereco da Pessoa",default=None)
    pessoa_email = models.CharField(max_length = 100,verbose_name="Email da Pessoa",default=None)
    pessoa_imagem = models.ImageField(upload_image_formater, default=None, blank=True, null=True)
    # pessoa_senha =  models.CharField(max_length = 100,verbose_name="Senha da Pessoa",default='Senha', blank=False, null=False)
    pessoa_usuario = models.ForeignKey(allauth_app_settings.USER_MODEL, verbose_name="usuario", on_delete=models.RESTRICT, default=None, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.pessoa_nome, self.pessoa_telefone,self.pessoa_email, self.pessoa_created, self.ativo, self.pessoa_endereco)

    class Meta:
        ordering = ('pessoa_nome','pessoa_endereco')
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Pessoas_Juridicas(Pessoas):
    pj_atividade = models.CharField(max_length = 100,verbose_name="Atividades da empresa",default=None)
    pj_cnpj = models.CharField(max_length = 100,verbose_name="CNPJ da empresa",default=None)
    pj_servico = models.CharField(max_length = 100,verbose_name="Servico da empresa",default=None)

    def __str__(self):
        return '%s %s %s' % (self.pj_atividade, self.pj_cnpj, self.pj_servico)

    class Meta:
        ordering = ('pj_atividade',)
        verbose_name = 'Pessoas_Juridica'
        verbose_name_plural = 'Pessoas_Juridicas'


class Pessoas_Fisicas(Pessoas):
    pf_cpf = models.CharField(max_length = 100,verbose_name="CPF da Pessoa",default=None)
    pf_datanascimento = models.DateField(max_length = 100,verbose_name="Data de Nascimento",default=None)
    pf_fidelidade = models.CharField(max_length = 100,verbose_name="Fidelidade da Pessoa",default=None)

    def __str__(self):
        return '%s %s %s' % (self.pf_cpf, self.pf_datanascimento, self.pf_fidelidade)

    class Meta:
        ordering = ('pf_cpf','pf_datanascimento')
        verbose_name = 'Pessoa_Fisica'
        verbose_name_plural = 'Pessoas_Fisicas'


class Horarios(models.Model):
    horarioCreated = models.DateTimeField(verbose_name="TimeStamp", auto_now_add=True)
    ativo = models.CharField(max_length =1,default="S")
    horario_empresa = models.CharField(max_length = 100,verbose_name="Horario da empresa",default=None)
    horario_pessoas = models.CharField(max_length = 100,verbose_name="Horario Pessoa",default=None)
    horario_local = models.CharField(max_length = 100,verbose_name="Horario Local",default=None)
    horario_servico = models.CharField(max_length = 100,verbose_name="Horario Servico",default=None)
    horario_duracao = models.DateField(max_length = 100,verbose_name="horario duracao",default=None)
    horario_inicio = models.DateField(max_length = 100,verbose_name="horario inicio",default=None)
    horario_tipo = models.CharField(max_length = 100,verbose_name="horario tipo",default=None)  

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.horario_empresa, self.horario_pessoas, self.horario_local, self.horario_servico, self.horario_duracao, self.horario_inicio, self.horario_tipo)

    class Meta:
        ordering = ('horario_servico', 'horario_empresa', 'horario_pessoas')
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

class Locais(models.Model):
    localCreated = models.DateTimeField(verbose_name="TimeStamp", auto_now_add=True)
    ativo = models.CharField(max_length =1,default=None)
    local_nome = models.CharField(max_length = 100,verbose_name="Nome do Local",default=None)
    local_endereco = models.CharField(max_length = 100,verbose_name="Endereco do Local",default=None)
    local_descricao = models.CharField(max_length = 100,verbose_name="Descricao do Local",default=None)   


    def __str__(self):
        return '%s %s %s' % (self.local_nome, self.local_endereco, self.local_descricao)

    class Meta:
        ordering = ('local_nome', 'local_endereco', 'local_descricao')
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

class Calendario(models.Model):
    
    TIMEBLOCK_CHOICES = (
        ("A", "9:00-10:00"),
        ("B", "10:00-11:00"),
        ("C", "11:00-12:00"),
        ("D", "14:00-15:00"),
        ("E", "15:00-16:00"),
        ("F", "16:00-17:00"),
        ("G", "17:00-18:00"),
        ("H", "18:00-19:00"),
        ("I", "19:00-20:00"),
        ("J", "20:00-21:00"),     
    )

    date_posted = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    timeblock = models.CharField(max_length=10, choices=TIMEBLOCK_CHOICES, default="A")

    nome_completo = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=30, default="")
    serviço = models.CharField(max_length=50, default="")

    # @property
    def is_upcoming(self):
        return date.today() <= self.date

    is_upcoming.admin_order_field = "date"
    is_upcoming.boolean = True
    is_upcoming.short_description = "Session in the future?"

    @property
    def get_weekday(self):
        return self.date.strftime("%A")

    def __str__(self) -> str:
        return f"{self.nome_completo}: {self.date} ({self.timeblock})"

    def get_absolute_url(self):
        # returns a complete url string and let view handle the redirect
        return reverse("session-detail", kwargs={"pk": self.pk})
