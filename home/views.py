from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import ContatoForm, ProdutoForm
from .models import Produto


# 🌐 Páginas gerais
def index(request):
    return render(request, "index.html", {"mensagem": "Bem-vindo ao nosso Sistema"})


def sobre(request):
    return render(request, "sobre.html", {"mensagem": "Sobre o sistema"})


def contato(request):
    form = ContatoForm()
    return render(request, "contato.html", {"form": form})


def ajuda(request):
    return render(request, "ajuda.html")


def exibir_item(request, id):
    return render(request, "exibir_item.html", {"id": id})


def exibir_perfil(request, usuario):
    return render(request, "exibir_perfil.html", {"usuario": usuario})


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
    return render(
        request,
        "dia_da_semana.html",
        {
            "dia": dia,
            "titulo": f"Dia da Semana - {dia}",
            "conteudo": f"O dia da semana {num} corresponde a {dia}!",
        },
    )


# 📦 Produtos (CRUD no banco)
def produto(request):
    lista = Produto.objects.all().order_by("id")
    return render(request, "produto/lista.html", {"lista": lista})


def form_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("produto")
    else:
        form = ProdutoForm()

    return render(request, "produto/formulario.html", {"form": form})


def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, "produto/detalhes.html", {"produto": produto})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("produto")
    else:
        form = ProdutoForm(instance=produto)

    return render(request, "produto/formulario.html", {"form": form, "produto": produto})


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.delete()
        return redirect("produto")

    return render(request, "produto/excluir.html", {"produto": produto})
