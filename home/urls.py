from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('ajuda/', views.ajuda, name="ajuda"),
    path('item/<int:id>', views.exibir_item, name="exibir_item"),
    path('perfil/<str:usuario>', views.exibir_perfil, name="exibir_perfil"),
    path('diasemana/<int:num>/', views.dia_da_semana, name='dia_da_semana'),

    # Produtos
    path('produto/', views.produto, name='produto'),
    path('produto/form', views.form_produto, name='form_produto'),

    # Novas rotas
    path('produto/<int:id>/detalhes/', views.detalhes_produto, name='detalhes_produto'),
    path('produto/<int:id>/editar/', views.editar_produto, name='editar_produto'),
    path('produto/<int:id>/excluir/', views.excluir_produto, name='excluir_produto'),
]
