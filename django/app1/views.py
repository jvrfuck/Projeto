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
def db1(request):
  data = "Versao 0.01 - Dashboard 1 (um)"

  return render(request, 'dashboard1.html', {'dados': data})

@login_required
def db2(request):
  data = "ersao 0.01 - Dashboard 2 (dois)"

  return render(request, 'dashboard2.html', {'dados': data})
