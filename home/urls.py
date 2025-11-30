from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    
    #Rota para pagina Inicial Raiz
    path('', views.index, name="index"),
    
    #Pagina Sobre
    path('sobre/', views.sobre, name="sobre"),
    
    #Pagina para Contatos
    path("contato/", views.contato, name="contato"), 
    
    #Pagina de Ajuda
    path("ajuda/", views.ajuda, name="ajuda")

]