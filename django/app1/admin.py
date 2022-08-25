from django.contrib import admin

# Register your models here.

from .models import Empresas, Pessoas, Locais, Servicos, Horarios
admin.site.register(Empresas)
admin.site.register(Pessoas)
admin.site.register(Locais)
admin.site.register(Servicos)
admin.site.register(Horarios)