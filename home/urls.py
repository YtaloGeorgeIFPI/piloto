from django.contrib import admin
from django.urls import path
from . import views  # Certifique-se de importar as views do mesmo diretório (home)

urlpatterns = [
    # Rota para página Inicial Raiz
    path('', views.index, name="index"),
    
    # Página Sobre
    path('sobre/', views.sobre, name="sobre"),
    
    # Página para Contatos
    path("contato/", views.contato, name="contato"), 
    
    # Página de Ajuda
    path("ajuda/", views.ajuda, name="ajuda"),  
    
    # Página de Exibição de Item
    path('item/<int:id>', views.exibir_item, name="exibir_item"),

    # Página de Perfil
    path('perfil/<str:usuario>', views.exibir_perfil, name="exibir_perfil"),

    # Rota para o dia da semana
    path('diasemana/<int:num>/', views.dia_da_semana, name='dia_da_semana'),
  # Corrigido

    # Adicionando a URL para 'produto'
    path('produto/', views.produto, name='produto'),  # Adicionando a URL para 'produto'

    # Outras URLs...
]
