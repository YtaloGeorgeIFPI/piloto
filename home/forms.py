# home/forms.py
from django import forms
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label="Nome Completo",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome completo"}),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "E-mail"})
    )

    telefone = forms.CharField(
        max_length=15,
        label="Telefone / WhatsApp",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "(99) 99999-9999"}),
    )

    assunto = forms.ChoiceField(
        label="Assunto do Contato",
        choices=[
            ("suporte", "Suporte técnico"),
            ("comercial", "Comercial"),
            ("reclamacao", "Reclamação"),
            ("parceria", "Parceria"),
            ("financeiro", "Financeiro"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Escreva sua mensagem", "rows": 10}
        )
    )


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "preco"]
        labels = {
            "nome": "Nome do Produto",
            "preco": "Preço",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: Impressora"}),
            "preco": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ex: 600.00"}),
        }
