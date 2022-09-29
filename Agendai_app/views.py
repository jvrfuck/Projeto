from django.http.response import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib import messages
from .models import Agendamento
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} do Agendaí.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return 


class AgendamentoTemplateView(TemplateView):
    template_name = "agendamentos/agendamento.html"


    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")

        appointment = Agendamento.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Obrigado, {fname}, por ter solicitado uma consulta!")
        return HttpResponseRedirect(request.path)


class GerenciamentoAgendamentoTemplateView(ListView):
    template_name = "agendamentos/gerenciamento-agendamento.html"
    model = Agendamento
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Agendamento.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('agendamentos/email.html').render(data)
        email = EmailMessage(
            "Sobre o seu agendamento",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"Você aceitou o agendamento de {appointment.first_name}")
        return HttpResponse(request.path)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Agendamento.objects.all()
        context.update({
            "title":"Manage Appointments"
        })
        return context
