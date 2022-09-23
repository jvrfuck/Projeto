from django.contrib import admin
from .models import Pessoas
from .models import Pessoas_Fisicas
from .models import Locais
from .models import Pessoas_Juridicas
from .models import Horarios


admin.site.register(Pessoas)
admin.site.register(Locais)
admin.site.register(Pessoas_Fisicas)
admin.site.register(Pessoas_Juridicas)
admin.site.register(Horarios)