from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.

def envia_email(request):

    html_content = render_to_string('email/cadastro_confirmado.html')
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives('Cadastro confirmado',text_content,settings.EMAIL_HOST_USER,['forwest3@gmail.com'])
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return HttpResponse('olá')
