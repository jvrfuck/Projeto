from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('empresas/', views.empresas),
    path('pessoas/', views.pessoas),
    path('ag', views.ag),
    path('sobre', views.sobre),
    path('pessoas/add', views.pessoa_add),
    path('pessoas/edit/<int:id>', views.pessoa_edit, name="edit-pessoa"),
    path('pessoas/delete/<int:id>', views.pessoa_delete, name="delete-pessoa"),
    path('empresas/add', views.empresa_add),
    path('empresas/edit/<int:id>', views.empresa_edit, name="edit-empresa"),
    path('empresas/delete/<int:id>', views.empresa_delete, name="delete-empresa"),
]
