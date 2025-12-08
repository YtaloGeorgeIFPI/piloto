from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    # Aqui você pode passar o conteúdo desejado
    return render(request, "index.html", {'mensagem': 'Bem-vindo ao nosso Sistema'})

def sobre(request):
    return render(request, "sobre.html", {'mensagem': 'Sobre o sistema'})

def contato(request):
    # Aqui você pode passar o conteúdo desejado
    return render(request, "contato.html", {'mensagem': 'Entre em Contato'})


def ajuda(request):
    return render(request, "ajuda.html")

def exibir_item(request, id):
    return render(request, "exibir_item.html", {'id': id})

def exibir_perfil(request, usuario):
    return render(request, "exibir_perfil.html", {'usuario': usuario})

def dia_da_semana(request, num):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }

    if num < 1 or num > 7:
        return HttpResponse("Número inválido! Use um número entre 1 e 7.")
    
    dia = dias.get(num)
    return render(request, "dia_da_semana.html", {
        'dia': dia, 
        'titulo': f"Dia da Semana - {dia}", 
        'conteudo': f"O dia da semana {num} corresponde a {dia}!"
    })

def produto(request):
    return render(request, "produto.html")
