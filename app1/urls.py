from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld, name="home"),
    path('empresas/', views.empresas),
    path('pessoas/', views.pessoas),
    path('ag/', views.ag),
    path('sobre/', views.sobre),
    path('pessoa/add', views.pessoa_add),
    path('pessoa/edit/<int:id>', views.pessoa_edit, name="edit-pessoa"),
    path('pessoa/delete/<int:id>', views.pessoa_delete, name="delete-pessoa"),
    path('empresa/add', views.empresa_add),
    path('empresa/edit/<int:id>', views.empresa_edit, name="edit-empresa"),
    path('empresa/delete/<int:id>', views.empresa_delete, name="delete-empresa"),
    ##################################################################################
    path("sessions/", views.SessionListView.as_view(), name="scheduler-sessions"),
    path("sessions/<int:pk>/", views.SessionDetailView.as_view(), name="session-detail"),
    path("sessions/new/", views.SessionCreateView.as_view(), name="session-create"),
    path(
        "sessions/new/<date>/",
        views.SessionCreateView.as_view(),
        name="session-create-date",
    ),
    path(
        "sessions/new/<date>/<str:timeblock>",
        views.SessionCreateView.as_view(),
        name="session-create-spec",
    ),
    path("sessions/<int:pk>/edit", views.SessionEditView.as_view(), name="session-edit"),
    path(
        "sessions/<int:pk>/cancel", views.SessionCancelView.as_view(), name="session-cancel"),  
    path("sessions/home", views.home, name="scheduler-home"),
]
