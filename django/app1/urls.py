from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('empresas/', views.empresas),
    path('pessoas/', views.pessoas),
    path('ag', views.ag),
    path('sobre', views.sobre),
    path('pessoa_add', views.pessoa_add),
    path('pessoa_edit/<int:id>', views.pessoa_edit, name="edit-pessoa"),
    path('pessoa_delete/<int:id>', views.pessoa_delete, name="delete-pessoa"),
]
