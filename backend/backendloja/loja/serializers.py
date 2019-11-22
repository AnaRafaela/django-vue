from django.db import transaction
from rest_framework import serializers
from django.contrib.auth.models import User

from loja.models import (Produto, Categoria)

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('id', 'nome', 'descricao', 'foto', 'preco', 'categoria')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')
