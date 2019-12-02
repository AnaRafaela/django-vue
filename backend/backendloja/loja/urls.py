from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (ProdutoList,ProdutoGet, CategoriaList,CategoriaGet, CarrinhoCreate, CarrinhoGet,
CarrinhoList, CarrinhoUpdate, CarrinhoDestroy, ProdutoDetailGet)

urlpatterns = [
    path('produtos/', ProdutoList.as_view()),
    path('produtos/get/<int:categoria>/', ProdutoGet.as_view()),
    path('produto/get/<int:pk>/', ProdutoDetailGet.as_view()),
    path('categorias/', CategoriaList.as_view()),
    path('categorias/get/<int:pk>/', CategoriaGet.as_view()),
    path('carrinho/', CarrinhoList.as_view()),
    path('carrinho/<int:pk>/', CarrinhoDestroy.as_view()),
    path('books/add/', CarrinhoCreate.as_view()),
    path('books/get/<int:pk>/', CarrinhoGet.as_view()),
    path('books/edit/<int:pk>/', CarrinhoUpdate.as_view()),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
