from django import forms
from .models import Pessoas, Pessoas_Fisicas


class PessoasForm(forms.ModelForm):
    # pessoas_nome = forms.CharField(label='NomeX', max_length=100)
    # pessoas_cpf = forms.IntegerField(label='CPF')

    class Meta:
        model = Pessoas and Pessoas_Fisicas
        fields = ('ativo', 'pessoa_nome', 'pf_cpf', 'pf_datanascimento',
                  'pessoa_telefone', 'pessoa_endereco', 'pessoa_email', 'pf_fidelidade')