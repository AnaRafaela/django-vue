from django.contrib import admin
from loja.models import Produto, Categoria, Carrinho, ProdutoCarrinho
# Register your models here.


admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(ProdutoCarrinho)
