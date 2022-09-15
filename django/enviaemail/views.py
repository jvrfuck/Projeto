from django.core.mail import send_mail 
from django.conf import settings, redirect


# Create your views here.
def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['c.nardino3@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

    return redirect ('/accounts/login')
