from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmpresasForm, PessoasForm
from django.http import HttpResponseRedirect
from .models import Pessoas, Pessoas_Fisicas, Pessoas_Juridicas
from django.contrib import messages
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
def pessoas(request):
  search = request.GET.get('Search')
  if search:
      pessoas = Pessoas.objects.filter(pessoa_nome__icontains=search)
  else:
      pessoas = Pessoas.objects.all()

  return render(request, 'pessoas.html',
                  {'pessoas': pessoas})    

@login_required
def empresas(request):
    if request.method == 'POST':
        form = EmpresasForm(request.POST)
        if form.is_valid():
            nova_pessoa = form.save(commit=False)
            nova_pessoa.ativo = form.cleaned_data['ativo']
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pj_cnpj = form.cleaned_data['pj_cnpj']
            nova_pessoa.pj_atividade = form.cleaned_data['pj_atividade']
            nova_pessoa.pessoa_telefone = form.cleaned_data['pessoa_telefone']
            nova_pessoa.pessoa_endereco = form.cleaned_data['pessoa_endereco']
            nova_pessoa.pessoa_email = form.cleaned_data['pessoa_email']
            nova_pessoa.pj_servico = form.cleaned_data['pj_servico']
            nova_pessoa.save()
            return HttpResponseRedirect('/empresas/')
    else:
        form = EmpresasForm()
    empresas = Pessoas_Juridicas.objects.all()

    return render(request, 'empresas.html', {'form': form, 'empresas': empresas})  

@login_required
def pessoa_add(request, id=0):
    if request.method == 'POST':
        form = PessoasForm(request.POST)
        if form.is_valid():
            nova_pessoa = form.save(commit=False)
            nova_pessoa.ativo = form.cleaned_data['ativo']
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pf_cpf = form.cleaned_data['pf_cpf']
            nova_pessoa.pf_datanascimento = form.cleaned_data['pf_datanascimento']
            nova_pessoa.pessoa_telefone = form.cleaned_data['pessoa_telefone']
            nova_pessoa.pessoa_endereco = form.cleaned_data['pessoa_endereco']
            nova_pessoa.pessoa_email = form.cleaned_data['pessoa_email']
            nova_pessoa.pf_fidelidade = form.cleaned_data['pf_fidelidade']
            nova_pessoa.save()
            return HttpResponseRedirect('/pessoas')
    else:
        form = PessoasForm()
        
    pessoas = Pessoas.objects.all()

    return render(request, 'pessoa_add.html',
                    {
                        'form': form,
                        'pessoas': pessoas
                    }
                    )

@login_required
def pessoa_edit(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    form = PessoasForm(instance=pessoa)
    if ( request.method == 'POST'):
        form = PessoasForm(request.POST, instance=pessoa)
        if (form.is_valid()):
            pessoa.save()
            return redirect('/pessoas')
        else:
            return render(request, 'pessoa_edit.html', {'form': form, 'pessoa': pessoa})
    else:
        return render(request, 'pessoa_edit.html', {'form': form, 'pessoa': pessoa})

@login_required
def pessoa_delete(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    pessoa.delete()
    messages.info(request, 'Pessoa apagado do banco de dados')
    return redirect('/pessoas')
