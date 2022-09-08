```markdown

Salve jao, Na aula de hoje criamos 3 Novos templates (pessoas_add, pessoas_edit,pessoas_list) e excluimos o template de PESSSOAS (PESSOAS_VIEW), nao sei como vc tinha salvado.

```

```markdown

## Segue a baixo os 3 templates de Pessoas: 
<pessoas_edit>

{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block title %}{{pessoa.pessoa_nome}}{% endblock %}

{% block content %}
<div class="offset-1 col-10 list-div">
    <h1>Editando '{{pessoa.pessoa_nome}}'</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form|crispy }}
        <input type="submit" class="btn btn-success" value="Salvar">
    </form>
</div>
{% endblock %}


<pessoa_list>

{% extends 'base.html' %}

{% block title %}Pessoas{% endblock %}

{% block content %}
<div class="offset-1 col-10 list-div">
    <h1>Lista de Pessoas</h1>
    <div class="container dashboard">        
        <div class="col-6 dashboard-box" id="dashboard-done">
            {% if messages %}
            <ul class="messages">
                {% for message in messages %}
                <li{% if message.tags %} class="alert alert-{{ message.tags }}"{% endif %}>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %}

            <h4>Pessoas</h4>            
            <ul class="task-list">
                <div class="row">
                    <div class="col" >
                        <span text-left>ID</span>
                    </div>           
                    <div class="col">
                        <span>Nome</span>
                    </div>           
                    <div class="col">
                        <span>Idade</span>
                    </div>                
     
                    <div class="col">
                        <span><i class="fas fa-edit"></i></span>
                        <span><i class="fas fa-trash"></i></span>
                        <!-- <a href="/changestatus/{{i.id}}"><i class="fas fa-check"></i></a>  -->
                    </div>
                </div>

                


                {% for i in pessoas %}        
                <div class="row">
                    <div class="col" >
                        <span>{{i.id}}</span>
                    </div>           
                    <div class="col">
                        <span>{{i.pessoa_nome}}</span>
                    </div>           
                    <div class="col">
                        <span>{{i.pessoa_idade}}</span>
                    </div>                
     
                    <div class="col">
                        <a href="/pessoa_edit/{{i.id}}"><span><i class="fas fa-edit"></i></span></a>
                        <a href="/pessoa_delete/{{i.id}}" class="delete-btn"><span><i class="fas fa-trash"></i></span></a>        
                        <!-- <a href="/changestatus/{{i.id}}"><i class="fas fa-check"></i></a>  -->
                    </div>
                </div>
                {% endfor %}

                <div class="row">
                    <div class="col">
                        <a id="add-link" href="/pessoa_add">
                            <div class="add-div">
                                <i class="fas fa-plus"></i> Adicionar Pessoa
                            </div>
                        </a>                   
                    </div>
                    <div class="col">                        
                        <div class="search-div">
                            <form method="GET" id="search-form">
                                <input class="form-control" type="text" id="search" name="search" placeholder="Digite o nome para buscar..." value="{{ request.GET.search }}">
                                <i class="fas fa-search" id="search-btn"></i>
                            </form>
                        </div>
                    </div>
                </div>
            </ul>
        </div>
</div>
</div>
{% endblock %}

<pessoa_add>

{% extends 'base.html' %}

{% block title %}Pessoas{% endblock %}

{% block content %}
<div class="offset-1 col-10 list-div">
    <h1>Adicione Pessoa:</h1>
    <form action="" method="post" >    
        {% csrf_token %}  
        {{ form }}         
        <input type="submit" value="Submit">
    </form>   
</div>
{% endblock %}

```

```markdown	
No arquivo da base como foi mudado os templates, voce deve mudar o que esta dentro 

<base.html>

Mudar na linha 32 "/pessoas" (ou "/pessoasview", conforme estava sua pasta antiga) para "/pessoas_list" 

```

```markdown
Como foi criado as novas pastas tambem deve modificar os urls/views do App 

<Urls>
    path('pessoas_list/', views.pessoas_list),    
    path('pessoa_add', views.pessoa_add),
    path('pessoa_edit/<int:id>', views.pessoa_edit, name="edit-pessoa"),
    path('pessoa_delete/<int:id>', views.pessoa_delete, name="delete-pessoa"),

<Views>
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required
def pessoas_list(request):
    search = request.GET.get('search')
    if search:         
        pessoas = Pessoas.objects.filter(pessoa_nome__icontains=search)
    else:
        pessoas = Pessoas.objects.all()

    return render(request, 'pessoas_list.html',
                  {'pessoas': pessoas})


@login_required
def pessoa_add(request, id=0):

    if request.method == 'POST':
        form = PessoasForm(request.POST)
        if form.is_valid():
            nova_pessoa = form.save(commit=False)
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pessoa_idade = form.cleaned_data['pessoa_idade']
            nova_pessoa.save()
            return HttpResponseRedirect('/pessoas_list')
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
    if (request.method == 'POST'):
        form = PessoasForm(request.POST, instance=pessoa)
        if (form.is_valid()):
            pessoa.save()
            return redirect('/pessoas_list')
        else:
            return render(request, 'pessoa_edit.html', {'form': form, 'pessoa': pessoa})
    else:
        return render(request, 'pessoa_edit.html', {'form': form, 'pessoa': pessoa})


# @login_required
# def thanks(request):
#     mensagem = "Obrigado!"
#     return render(request, 'thanks.html', {'mensagem': mensagem}
                #   )


@login_required
def pessoa_delete(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    pessoa.delete()
    messages.info(request, 'Pessoa apagada do banco de dados')
    return redirect('/pessoas_list')

```

```markdown	

## opcional

Como o professor nao ta mais usando no site o thanks, dashboards e etc, eu ja exclui a pasta do template, na url e no views e nao deu problema e deu uma limpada visualmente, fica a opçao pra vc ai.

```