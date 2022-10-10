from django import forms
from numpy import deprecate_with_doc
from .models import Calendario, Pessoas, Pessoas_Fisicas, Pessoas_Juridicas, Calendario


class PessoasForm(forms.ModelForm):
    class Meta:
        model = Pessoas and Pessoas_Fisicas
        fields = ('pessoa_nome', 'pf_cpf', 'pf_datanascimento',
                  'pessoa_telefone', 'pessoa_endereco', 'pessoa_email', 'pf_fidelidade')

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Pessoas and Pessoas_Juridicas
        fields = ('pessoa_nome', 'pj_cnpj', 'pj_atividade',
                  'pessoa_telefone', 'pessoa_endereco', 'pessoa_email', 'pj_servico')

class SessionForm(forms.ModelForm):
    date = forms.DateField(disabled=True)
    # timeblock = forms.CharField(disabled=True)
    nome_completo = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "insira seu nome"}), required=False
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "informe seu email"}), required=False
    )
    serviço = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "informe o procedimento desejado"}), required=False
    )

    class Meta:
        model = Calendario
        fields = ["date", "timeblock", "nome_completo", "email", "serviço"]