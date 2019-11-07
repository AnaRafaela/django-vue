from django.urls import path

from .views import (ProdutoList, CategoriaList)

urlpatterns = [
    path('produtos/', ProdutoList.as_view()),
    path('categorias/', CategoriaList.as_view()),
]
