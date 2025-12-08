from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")

def ajuda(request):
    return render(request, "ajuda.html")

def exibir_item(request, id):
    return render(request, "exibir_item.html", {'id':id})

def exibir_perfil(request, usuario):
    return render(request, "exibir_perfil.html", {'usuario':usuario})

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

    # Verifica se o número está entre 1 e 7
    if num < 1 or num > 7:
        return HttpResponse("Número inválido! Use um número entre 1 e 7.")
    
    # Obtém o dia correspondente
    dia = dias.get(num)
    return render(request, "dia_da_semana.html", {'dia': dia})

