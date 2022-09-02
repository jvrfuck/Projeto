from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

