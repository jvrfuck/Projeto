from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('db1', views.db1),
    path('db2', views.db2)
]
