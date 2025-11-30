from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return HttpResponse("A viw index funcionou, Wow, parabéns!")

def sobre(request):
    return HttpResponse("<h1>Pagina Home</h1>")

def contato(request):
    return HttpResponse("<h1>Esta é a pagina de contato</h1>")

def ajuda(request):
    return HttpResponse("<h1>Esta é a pagina de ajuda</h1>")