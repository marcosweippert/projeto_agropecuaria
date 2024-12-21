from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)  # Ex: "Grãos", "Vegetais"
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.PositiveIntegerField(blank=True, null=True)
    unidade = models.CharField(max_length=20)  # Ex: "kg", "litros"
    safra = models.DateField()
    descricao = models.TextField(blank=True, null=True)  # Descrição detalhada do produto
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Foto do produto
    quantidade_minima_estoque = models.PositiveIntegerField(default=0, blank=True, null=True)  # Estoque mínimo
    validade = models.DateField(blank=True, null=True)  # Data de validade
    fornecedor = models.CharField(max_length=100, blank=True, null=True)  # Nome do fornecedor
    local_armazenamento = models.CharField(max_length=100, blank=True, null=True)  # Ex: "Armazém 1"
    data_entrada = models.DateField(auto_now_add=True, blank=True, null=True)  # Data de entrada no estoque
    ultima_atualizacao = models.DateTimeField(auto_now=True)  # Data da última atualização
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Peso bruto
    peso_liquido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Peso líquido
    codigo_barras = models.CharField(max_length=13, unique=True, blank=True, null=True)  # Código de barras
    quantidade_reservada = models.PositiveIntegerField(default=0)  # Quantidade reservada para pedidos
    ativo = models.BooleanField(default=True, blank=True, null=True)  # Indica se o produto está ativo para vendas
    marca = models.CharField(max_length=50, blank=True, null=True)  # Marca do produto
    tipo_embalagem = models.CharField(max_length=50, blank=True, null=True)  # Tipo de embalagem, ex: "Saco", "Caixa"
    quantidade_por_embalagem = models.PositiveIntegerField(blank=True, null=True)  # Quantidade por unidade de embalagem
    origem = models.CharField(max_length=50, blank=True, null=True)  # Origem do produto, ex: "Nacional", "Importado"

    def __str__(self):
        return self.nome

    def estoque_disponivel(self):
        """
        Calcula o estoque disponível subtraindo a quantidade reservada.
        """
        return self.estoque - self.quantidade_reservada

    def estoque_insuficiente(self):
        """
        Verifica se o estoque disponível está abaixo do nível mínimo.
        """
        return self.estoque_disponivel() < self.quantidade_minima_estoque
