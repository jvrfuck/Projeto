from django.urls import path
from .views import HomeTemplateView, AgendamentoTemplateView, GerenciamentoAgendamentoTemplateView


urlpatterns = [
    path("", HomeTemplateView.as_view(), name = "home"),
    path("agendai/", AgendamentoTemplateView.as_view(), name = "agendamento"),
    path("gerenciamento-agendamentos/", GerenciamentoAgendamentoTemplateView.as_view(), name = "gerenciamento")
]
