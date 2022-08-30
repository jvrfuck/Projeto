## Fazer o PIP e incluir no requirements.txt
pip install django-crispy-forms
pip freeze > requirements.txt
## PARTE APP
#<<Na pasta templates fazer os corpos do site>>
#<<base.html>>
#nessa primeira aonde tem o dashboard e area1 e etc e onde ficam os nomes dos campos na parte superior


{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">    
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    
    
</head>
<body>
    <div class="container-fluid">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="/">By myself</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="/db1">Area1</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/db2">DashBoard2</a>
                    </li>
                    <li class="nav-item">
                            <a class="nav-link" href="/admin">Admin</a>
                        </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="/accounts/login">Login</a>
                    </li>
                    {% endif %}
                    <li class="nav-item">
                        <a class="nav-link" href="/about">Sobre</a>
                    </li>
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                            <a class="nav-link" href="/accounts/logout">Sair </a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </nav>
        {% block content %}
        {% endblock %}
        <footer>
            <p>App By eu</p>
        </footer>
    </div>
    <script
    src="https://code.jquery.com/jquery-3.4.0.min.js"
    integrity="sha256-BJeo0qm959uMBGb65z40ejJYGSgR7REI4+CW1fNKwOg="
    crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js" integrity="sha384-xrRywqdh3PHs8keKZN+8zzc5TX0GRTLCcmivcbNJWm2rs5C8PRhcEn3czEjhAO9o" crossorigin="anonymous"></script>
    <script src="{% static 'js/scripts.js' %}"></script>
</body>
</html>

#<<index.html>>

{% extends 'base.html'%}

{% block title %}Lista de Tags{% endblock %}

{% block content %}
<div class="row">
    <div class="col">
                <h4 class="card-title text-center">DashBoard1</h4>        
                    {% csrf_token %}  
                    {{ dados }}

    </div>
</div>

{% endblock %}

#<<Dashboard1.html>>


#<<baixar pasta Static do repositorio do professor>>
#<<Na pasta views.py adicionar>>

from django.contrib.auth.decorators import login_required

<!-- #em cima do Def -->
@login_required

#<<Para fazer novas "frontsend", Para isso o nome que sera usado ai em request, deve ser o mesmo que esta na base.html dos templates EX:>>

@login_required
def db1(request):

    versao = "versao 0.00 de 19/08"

    return render(request, 'dashboard.html', 
        {'dados' : versao}


## na parte do projeto

#<<NA pasta Settings, adicionar>>

INSTALLED_APPS = [
    'accounts',
    'crispy_forms',
]
#<no final da pasta>
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(STATIC_URL, 'static/')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login'

#<se nao tiver feito o DIR nos templates>
'DIRS': [os.path.join(BASE_DIR, "templates")]

#<<na pasta Urls>>
path("accounts/",include("django.contrib.auth.urls")),

## CRiar pasta accounts

django-admin startapp accounts

#<<Copiar pasta de templates do repositorio do professor>>

<<na pasta views>>

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

#<<Criar pasta URLS>>

from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.SignUp.as_view(),name="register"),
]

