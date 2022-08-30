from django.contrib import admin

# Register your models here.

from .models import Pessoas_Fisicas, Pessoas, Locais, Pessoas_Juridicas, Horarios
admin.site.register(Pessoas_Juridicas)
admin.site.register(Pessoas)
admin.site.register(Locais)
admin.site.register(Pessoas_Fisicas)
admin.site.register(Horarios)