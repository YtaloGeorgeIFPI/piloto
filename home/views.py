# home/views.py

from django.shortcuts import render  # Importe render corretamente

# Views da aplicação 'home'
def index(request):
    return render(request, 'home/index.html')  # Supondo que você tenha um template 'index.html' no diretório 'home/templates/home'

def sobre(request):
    return render(request, 'home/sobre.html')  # Template 'sobre.html'

def contato(request):
    return render(request, 'home/contato.html')  # Template 'contato.html'

def ajuda(request):
    return render(request, 'home/ajuda.html')  # Template 'ajuda.html'
