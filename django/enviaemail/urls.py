from django.urls import path
from . import views 
from .views import HomeTemplateView, AppointmentTemplateView


urlpatterns = [
    path('email/', views.email, name='email'),
    path("", HomeTemplateView.as_view(), name = "home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name = "appointment")
]
