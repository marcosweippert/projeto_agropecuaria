# Generated by Django 5.1.3 on 2024-11-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf_cnpj', models.CharField(max_length=20, unique=True)),
                ('contato', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
    ]
