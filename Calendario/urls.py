from django.urls import path
from . import views


app_name = 'Calendario'
urlpatterns = [
    path('', views.index),
    path('calendar/', views.CalendarView.as_view())
]
