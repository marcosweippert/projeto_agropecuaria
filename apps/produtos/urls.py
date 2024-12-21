from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('criar/', views.criar_produto, name='criar_produto'),
    # Outras URLs relacionadas a produtos
]