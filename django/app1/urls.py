from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('empresas/list/', views.empresas),
    path('pessoas/list/', views.pessoas),
    path('ag', views.ag),
    path('sobre', views.sobre),
    path('pessoa/add', views.pessoa_add),
    path('pessoa/edit/<int:id>', views.pessoa_edit, name="edit-pessoa"),
    path('pessoa/delete/<int:id>', views.pessoa_delete, name="delete-pessoa"),
    path('empresa/add', views.empresa_add),
    path('empresa/edit/<int:id>', views.empresa_edit, name="edit-empresa"),
    path('empresa/delete/<int:id>', views.empresa_delete, name="delete-empresa"),
]
