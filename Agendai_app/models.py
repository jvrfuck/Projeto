from django.db import models

class Agendamento(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.CharField(max_length=50, null=True, blank=True)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    dia= models.DateField(auto_now_add=True, null=True, blank=True)


    def __str__ (self):
        return '%s %s %s %s %s %s %s' % (self.first_name, self.last_name, self.email, self.phone, self.cpf, self.nascimento, self.dia)

    class Meta:
        ordering = ["-sent_date"]