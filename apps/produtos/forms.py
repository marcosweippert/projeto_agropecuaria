# produtos/forms.py
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'preco', 'custo', 'estoque', 'unidade', 'safra', 'descricao', 'foto', 'quantidade_minima_estoque', 'validade', 'fornecedor']
