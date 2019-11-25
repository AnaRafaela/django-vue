from django.db import models
from django.contrib.auth.models import User

from loja.models.categoria import Categoria


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    foto = models.ImageField(upload_to='imagens')
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    produto = models.ManyToManyField('Produto')

    def __str__(self):
        return str((self.produto))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinho'

class ProdutoCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)

    def __str__(self):
        return str((self.produto, self.carrinho))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProdutoCarrinho'
        verbose_name_plural = 'ProdutoCarrinhos'


