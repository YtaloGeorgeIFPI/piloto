# Arquivo: home/urls.py

from django.urls import path
from . import views  # Importe as views que você criou

urlpatterns = [
    path('', views.index, name='index'),  # A URL raiz do app 'home' chama a função 'index' em views.py
    path('sobre/', views.sobre, name='sobre'),  # Página sobre
    path('contato/', views.contato, name='contato'),  # Página de contato
    path('ajuda/', views.ajuda, name='ajuda'),  # Página de ajuda
]
