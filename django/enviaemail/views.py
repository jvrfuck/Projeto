from django.http.response import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail 
from django.conf import settings, redirect


# Create your views here.
# Nosso envio de e-mail para usuários (pós registro deles)
def email(request):
    subject = 'Obrigado por se registar em nosso site'
    message = ' .. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['agendaieletronica@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

    return redirect ('/accounts/login')

# Entrada em contato de pessoas/empresas conosco
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
        return HttpResponse("Seu e-mail foi enviado!")

# Classe para agendamento (não sei se vai dar assim)
class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")

        messages.add_message(request, messages.SUCCESS, f"{message}")
        return HttpResponseRedirect(request.path)