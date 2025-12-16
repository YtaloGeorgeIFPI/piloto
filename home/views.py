from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContatoForm, ProdutoForm

# 🔁 Lista simulada de produtos
def produto_lista():
    return [
        {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
        {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
        {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
        {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
        {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
        {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
        {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
        {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
        {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
        {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
        {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
        {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
        {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
    ]

# 🌐 Páginas gerais
def index(request):
    return render(request, "index.html", {'mensagem': 'Bem-vindo ao nosso Sistema'})

def sobre(request):
    return render(request, "sobre.html", {'mensagem': 'Sobre o sistema'})

def contato(request):
    form = ContatoForm()
    context = {'form': form}
    return render(request, "contato.html", context)

def ajuda(request):
    return render(request, "ajuda.html")

def exibir_item(request, id):
    return render(request, "exibir_item.html", {'id': id})

def exibir_perfil(request, usuario):
    return render(request, "exibir_perfil.html", {'usuario': usuario})

def dia_da_semana(request, num):
    dias = {
        1: "Domingo", 2: "Segunda-feira", 3: "Terça-feira",
        4: "Quarta-feira", 5: "Quinta-feira", 6: "Sexta-feira", 7: "Sábado",
    }

    if num < 1 or num > 7:
        return HttpResponse("Número inválido! Use um número entre 1 e 7.")

    dia = dias.get(num)
    return render(request, "dia_da_semana.html", {
        'dia': dia,
        'titulo': f"Dia da Semana - {dia}",
        'conteudo': f"O dia da semana {num} corresponde a {dia}!"
    })

# 📦 Produtos
def produto(request):
    contexto = {'lista': produto_lista()}
    return render(request, 'produto/lista.html', contexto)

def form_produto(request):
    form = ProdutoForm()
    context = {'form': form}
    return render(request, "produto/formulario.html", context)

# 🔍 Detalhes do produto
def detalhes_produto(request, id):
    produto = next((p for p in produto_lista() if p['id'] == id), None)
    return render(request, 'produto/detalhes.html', {'produto': produto})

# ✏️ Edição do produto
def editar_produto(request, id):
    produto = next((p for p in produto_lista() if p['id'] == id), None)
    form = ProdutoForm(initial={'nome': produto['nome'], 'preco': produto['preco']})
    return render(request, 'produto/formulario.html', {'form': form, 'produto': produto})

# ❌ Exclusão com confirmação
def excluir_produto(request, id):
    produto = next((p for p in produto_lista() if p['id'] == id), None)

    if request.method == 'POST':
        # Aqui você poderia excluir de verdade se estivesse usando banco de dados
        return redirect('produto')  # redireciona para a lista após "exclusão"

    return render(request, 'produto/excluir.html', {'produto': produto})
