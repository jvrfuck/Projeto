from django.core.mail import send_mail 
from django.conf import settings, redirect


# Create your views here.
def email(request):
    subject = 'Obrigado por se registar em nosso site'
    message = ' .. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['agendaieletronica@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

    return redirect ('/accounts/login')
