from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('cadastrar_usuario', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario/$', views.logar_usuario, name="logar_usuario"),
    path('logout', views.logout, name="logout"),
    path('dadospessoais', views.dadospessoais, name="dadospessoais"),
    ]
