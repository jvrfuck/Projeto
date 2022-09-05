from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('empresas/', views.empresas),
    path('pessoas/', views.pessoas),
    path('ag', views.ag),
    path('sobre', views.sobre)
]
