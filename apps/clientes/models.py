from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    contato = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome