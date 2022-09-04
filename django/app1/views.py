from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Pessoas_FisicasForm
from django.http import HttpResponseRedirect
from .models import Pessoas, Pessoas_Fisicas

# Create your views here.

@login_required
def helloworld(request):

    versao = "Versão 0.00 de 25/08/2022 09:00"

    return render(request, 'index.html',
        {'data' : versao }
    )

@login_required
def emp(request):
  data = "Versao 0.01 - Cadastro Empresas"

  return render(request, 'empresas.html', {'dados': data})

@login_required
def pes(request):
  data = "Versao 0.01 - Cadastro de Pessoas"

  return render(request, 'pessoas.html', {'dados': data})

@login_required
def ag(request):
  data = "Versao 0.01 - Agendamentos"

  return render(request, 'agendamento.html', {'dados': data})


@login_required
def sobre(request):
  data = "Versao 0.01 - Sobre"

  return render(request, 'sobre.html', {'dados': data})  



@login_required
def pessoasview(request):

    if request.method == 'POST':
        form = Pessoas_FisicasForm(request.POST)
        if form.is_valid():
            nova_pessoa = form.save(commit=False)
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pessoa_telefone = form.cleaned_data['pessoa_telefone']
            nova_pessoa.pessoa_endereco = form.cleaned_data['pessoa_enderepessoa_datanascimento']
            nova_pessoa.pessoa_email = form.cleaned_data['pessoa_email']
            nova_pessoa.ativo = form.cleaned_data['ativo']
            nova_pessoa.pf_cpf = form.cleaned_data['pf_cpf']
            nova_pessoa.pf_datanascimento = form.cleaned_data['pf_datanascimento']
            nova_pessoa.pf_fidelidade = form.cleaned_data['pf_fidelidade']
            nova_pessoa.save()
            return HttpResponseRedirect('/pessoas/')
    else:   
        form = Pessoas_FisicasForm()

    pessoas = Pessoas_Fisicas.objects.all()

    return render(request, 'pessoasview.html',
                  {
                      'form': form,
                      'pessoas' : pessoas
                  }

                  )
