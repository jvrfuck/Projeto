from socket import fromshare
from django import forms
from .models import Pessoas_Fisicas, Pessoas

class Pessoas_FisicasForm(forms.ModelForm):
    class Meta:
        model = Pessoas_Fisicas and Pessoas
        fields = ('pessoa_nome', 'pessoa_telefone', 'pessoa_endereco', 'pessoa_email',
        'ativo','pessoa_created','pf_cpf','pf_datanascimento','pf_fidelidade')