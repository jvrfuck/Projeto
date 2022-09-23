from .models import Agendamento

def get_notification(request):
    count = Agendamento.objects.filter(accepted=False).count()
    data = {
        "count":count
    }
    return data