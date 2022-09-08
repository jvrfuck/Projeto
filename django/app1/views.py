from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmpresasForm, PessoasForm
from django.http import HttpResponseRedirect
from .models import Pessoas, Pessoas_Juridicas, Pessoas_Fisicas
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

  return render(request, 'empresas/list.html', {'dados': data})

@login_required
def pes(request):
  data = "Versao 0.01 - Cadastro de Pessoas"

  return render(request, 'pessoas/list.html', {'dados': data})

@login_required
def ag(request):
  data = "Versao 0.01 - Agendamentos"

  return render(request, 'agendamento.html', {'dados': data})


@login_required
def sobre(request):
  data = "Versao 0.01 - Sobre"

  return render(request, 'sobre.html', {'dados': data})  
   
@login_required
def empresas(request):
    search = request.GET.get('search')
    if search:
      empresas = Pessoas_Juridicas.objects.filter(pessoa_nome__icontains=search)
    else:
      empresas = Pessoas_Juridicas.objects.all()

    return render(request, 'empresas/list.html',
                  {'empresas': empresas})  

@login_required
def empresa_add(request, id=0):
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
            return HttpResponseRedirect('/empresas/list/')
    else:
        form = EmpresasForm()
    empresas = Pessoas_Juridicas.objects.all()

    return render(request, 'empresas/add.html', {'form': form, 'empresas': empresas})

@login_required
def empresa_edit(request, id):
    empresa = get_object_or_404(Pessoas_Juridicas, pk=id)
    form = EmpresasForm(instance=empresa)
    if ( request.method == 'POST'):
        form = EmpresasForm(request.POST, instance=empresa)
        if (form.is_valid()):
            empresa.save()
            return redirect('/empresas/list')
        else:
            return render(request, 'empresas/edit.html', {'form': form, 'empresa': empresa})
    else:
        return render(request, 'empresas/edit.html', {'form': form, 'empresa': empresa})

@login_required
def empresa_delete(request, id):
    empresa = get_object_or_404(Pessoas_Juridicas, pk=id)
    empresa.delete()
    messages.info(request, 'PJ apagado do banco de dados')
    return redirect('/empresas/list')

@login_required
def pessoas(request):
  search = request.GET.get('search')
  if search:
      pessoas = Pessoas.objects.filter(pessoa_nome__icontains=search)
  else:
      pessoas = Pessoas.objects.all()

  return render(request, 'pessoas/list.html',
                  {'pessoas': pessoas})

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
            return HttpResponseRedirect('/pessoas/list')
    else:
        form = PessoasForm()
        
    pessoas = Pessoas.objects.all()

    return render(request, 'pessoas/add.html',
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
            return redirect('/pessoas/list')
        else:
            return render(request, 'pessoas/edit.html', {'form': form, 'pessoa': pessoa})
    else:
        return render(request, 'pessoas/edit.html', {'form': form, 'pessoa': pessoa})

@login_required
def pessoa_delete(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    pessoa.delete()
    messages.info(request, 'Pessoa apagado do banco de dados')
    return redirect('/pessoas/list')
