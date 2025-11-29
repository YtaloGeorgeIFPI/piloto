# Arquivo: pweb/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # Aqui, a URL raiz vai diretamente para 'home.urls'
    path('admin/', admin.site.urls),  # URL para o painel administrativo
]
