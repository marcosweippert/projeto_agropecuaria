# Generated by Django 5.1.3 on 2024-11-08 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Em andamento', 'Em andamento'), ('Concluído', 'Concluído'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=15)),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]
