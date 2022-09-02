from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('emp', views.emp),
    path('pes', views.pes),
    path('ag', views.ag),
    path('sobre', views.sobre)
]
