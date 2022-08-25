from django.shortcuts import render

# Create your views here.


def helloworld(request):

    versao = "Versão 0.00 de 25/08/2022 09:00"

    return render(request, 'about.html',
        {'data' : versao }
    )