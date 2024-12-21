from django.db import models
from apps.produtos.models import Produto

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    produtos = models.ManyToManyField(Produto, related_name="fornecedores")
    contato = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome