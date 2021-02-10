from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.internacao, name ='internacao'),
    path('add_Ala/', views.add_Ala, name = 'add_Ala'),
    path('novo_paciente', views.novoPaciente, name='novo_paciente'),
    path('novo_internacao', views.novoInternacao, name='novo_internacao'),
    path('alta_internacao/<int:internacao>', views.altaInternacao, name='alta_internacao'),
    path('mover_internacao/<int:internacao>', views.moverInternacao, name='mover_internacao'),
    path('reservar_leito/<int:leito>', views.reservarLeito, name='reservar_leito'),
    path('cancelar_reserva/<int:leito>', views.cancelarReserva, name='cancelar_reserva'),
    path('boletim', views.boletim, name='boletim'),
    path('boletim_find', views.boletim_find, name='boletim_find'),
]

