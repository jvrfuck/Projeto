from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmpresasForm, PessoasForm
from django.http import HttpResponseRedirect
from .models import Calendario, Pessoas, Pessoas_Juridicas, Pessoas_Fisicas
from django.contrib import messages


# Create your views here.


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

  return render(request, 'agendamentos/agendamento.html', {'dados': data})

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
        if request.user.is_superuser:
            empresas = Pessoas_Juridicas.objects.all()
        elif request.user.is_authenticated:
            empresas = Pessoas_Juridicas.objects.filter(pessoa_usuario_id= request.user.id)   #filtrar o id da empresa da pessoa logada
        else:
            return redirect('/')

    return render(request, 'empresas/list.html',
                  {'empresas': empresas})  

@login_required
def empresa_add(request, id=0):
    if request.method == 'POST':
        form = EmpresasForm(request.POST)
        if form.is_valid():
            nova_pessoa = form.save(commit=False)
            # nova_pessoa.ativo = form.cleaned_data['ativo']
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pj_cnpj = form.cleaned_data['pj_cnpj']
            nova_pessoa.pj_atividade = form.cleaned_data['pj_atividade']
            nova_pessoa.pessoa_telefone = form.cleaned_data['pessoa_telefone']
            nova_pessoa.pessoa_endereco = form.cleaned_data['pessoa_endereco']
            nova_pessoa.pessoa_email = form.cleaned_data['pessoa_email']
            nova_pessoa.pj_servico = form.cleaned_data['pj_servico']
            nova_pessoa.save()
            return HttpResponseRedirect('/lista/empresas/')
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
            return redirect('/lista/empresas/')
        else:
            return render(request, 'empresas/edit.html', {'form': form, 'empresa': empresa})
    else:
        return render(request, 'empresas/edit.html', {'form': form, 'empresa': empresa})

@login_required
def empresa_delete(request, id):
    empresa = get_object_or_404(Pessoas_Juridicas, pk=id)
    empresa.delete()
    messages.info(request, 'PJ apagado do banco de dados')
    return redirect('/lista/empresas/')

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
            # nova_pessoa.ativo = form.cleaned_data['ativo']
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pf_cpf = form.cleaned_data['pf_cpf']
            nova_pessoa.pf_datanascimento = form.cleaned_data['pf_datanascimento']
            nova_pessoa.pessoa_telefone = form.cleaned_data['pessoa_telefone']
            nova_pessoa.pessoa_endereco = form.cleaned_data['pessoa_endereco']
            nova_pessoa.pessoa_email = form.cleaned_data['pessoa_email']
            nova_pessoa.pf_fidelidade = form.cleaned_data['pf_fidelidade']
            nova_pessoa.save()
            return HttpResponseRedirect('/lista/pessoas/')
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
            return redirect('/lista/pessoas/')
        else:
            return render(request, 'pessoas/edit.html', {'form': form, 'pessoa': pessoa})
    else:
        return render(request, 'pessoas/edit.html', {'form': form, 'pessoa': pessoa})

@login_required
def pessoa_delete(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    pessoa.delete()
    messages.info(request, 'Pessoa apagado do banco de dados')
    return redirect('/lista/pessoas/')

####################################################################
import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import SessionForm

def generate_daylist():
    daylist = []
    today = datetime.date.today()
    for i in range(7):
        day = {}
        curr_day = today + datetime.timedelta(days=i)
        weekday = curr_day.strftime("%A").upper()
        day["date"] = str(curr_day)
        day["day"] = weekday
        day["A_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="A").exists()
        )
        day["B_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="B").exists()
        )
        day["C_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="C").exists()
        )
        day["D_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="D").exists()
        )
        day["E_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="E").exists()
        )
        day["F_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="F").exists()
        )
        day["G_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="G").exists()
        )
        day["H_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="H").exists()
        )
        day["I_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="I").exists()
        )
        day["J_booked"] = (
            Calendario.objects.filter(date=str(curr_day)).filter(timeblock="J").exists()
        )
        # day["K_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="K").exists()
        # )
        # day["L_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="L").exists()
        # )
        # day["M_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="M").exists()
        # )
        # day["N_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="N").exists()
        # )
        # day["O_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="O").exists()
        # )
        # day["P_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="P").exists()
        # )
        # day["Q_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="Q").exists()
        # )
        # day["R_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="R").exists()
        # )
        # day["S_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="S").exists()
        # )
        # day["T_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="T").exists()
        # )
        # day["U_booked"] = (
        #     Calendario.objects.filter(date=str(curr_day)).filter(timeblock="U").exists()
        # )

        
        if day["day"] != "SUNDAY":  # Writing lab doesn't open on Saturday
            daylist.append(day)
    return daylist


class SessionListView(ListView):
    model = Calendario
    template_name = "calendario/sessions.html"  # <app>/<model>_<view_type>.html
    context_object_name = "sessions"
    ordering = ["-date"]


# saving code by following conventions
class SessionDetailView(DetailView):
    model = Calendario
    template_name = "calendario/session_detail.html"


# note: mixins should come before CreateView
class SessionCreateView(LoginRequiredMixin, CreateView):
    # model = Session
    # fields = ["date", "timeblock", "nome_completo", "email", "serviço "]
    form_class = SessionForm
    template_name = "calendario/session_form.html"

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {
            "date": self.kwargs.get("date"),
            "timeblock": self.kwargs.get("timeblock"),
        }


    # def get_form_kwargs(self, *args, **kwargs):  # forms.py def clean()
    #     kwargs = super(SessionCreateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs["user"] = self.request.user
    #     return kwargs


class SessionEditView(
    SuccessMessageMixin, LoginRequiredMixin, UpdateView
):
    model = Calendario
    fields = ["nome_completo", "email", "serviço"]
    # success_url = "/users/<str:username>/"
    success_message = "Session was updated successfully"
    template_name = "calendario/session_form.html"
    
    # def form_valid(self, form):
    #     form.instance.nome_completo = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        session = self.get_object()
        if self.request.user == session.nome_completo:
            return True
        return False
    


class SessionCancelView(LoginRequiredMixin, DeleteView):
    model = Calendario
    template_name = "calendario/session_confirm_delete.html"
    success_url = '/lista/sessions/home'
    
    def test_func(self):
        session = self.get_object()
        if self.request.user == session.nome_completo:
            return True
        return False


def home(request):
    context = {"days": generate_daylist()}
    return render(request, "calendario/home.html", context)


def about(request):
    return render(request, "calendario/about.html")


def sessions(request):
    context = {"sessions": Calendario.objects.all()}
    return render(request, "calendario/sessions.html", context)

