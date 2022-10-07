from django import forms
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
    course_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. Serviço"}), required=False
    )
    course_teacher = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. Empresa"}), required=False
    )
    helptype = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. Term paper"}), required=False
    )

    class Meta:
        model = Calendario
        fields = ["date", "timeblock", "course_name", "course_teacher", "helptype"]