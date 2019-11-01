from django.contrib import admin
from loja.models import Produto, Categoria
# Register your models here.


admin.site.register(Categoria)
admin.site.register(Produto)

