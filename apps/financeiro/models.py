from django.db import models
from apps.clientes.models import Cliente
from apps.fornecedores.models import Fornecedor

class Conta(models.Model):
    TIPO_CHOICES = [
        ('Receber', 'Receber'),
        ('Pagar', 'Pagar'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo} - {self.valor}"