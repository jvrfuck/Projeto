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
    path('empresa_add', views.empresa_add),
    path('empresa_edit', views.empresa_edit, name="edit-empresa"),
    path('empresa_delete', views.empresa_delete, name="delete-empresa"),
]
