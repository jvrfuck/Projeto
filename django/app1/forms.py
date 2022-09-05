from django import forms
from .models import Pessoas, Pessoas_Fisicas, Pessoas_Juridicas


class PessoasForm(forms.ModelForm):
    class Meta:
        model = Pessoas and Pessoas_Fisicas
        fields = ('ativo', 'pessoa_nome', 'pf_cpf', 'pf_datanascimento',
                  'pessoa_telefone', 'pessoa_endereco', 'pessoa_email', 'pf_fidelidade')

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Pessoas and Pessoas_Juridicas
        fields = ('ativo', 'pessoa_nome', 'pj_cnpj', 'pj_atividade',
                  'pessoa_telefone', 'pessoa_endereco', 'pessoa_email', 'pj_servico')