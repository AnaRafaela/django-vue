from django.db import transaction
from rest_framework import serializers
from django.contrib.auth.models import User

from loja.models import (Produto, Categoria, Carrinho, ProdutoCarrinho)

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('id', 'nome', 'descricao', 'foto', 'preco', 'categoria')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ('id', 'produto')

    @transaction.atomic
    def create(self, validated_data):
        carrinho = Carrinho.objects.create(**validated_data)
        if "produtos" in self.initial_data:
            produtos = self.initial_data.get("produtos")
            for produto in produtos:
                produto_id = produto.get("produto")
                produto_instance = Produto.objects.get(pk=produto_id)
                ProdutoCarrinho(carrinho=carrinho, produto=produto_instance).save()
        carrinho.save()
        return carrinho
