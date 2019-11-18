from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (ProdutoList, CategoriaList)

urlpatterns = [
    path('produtos/', ProdutoList.as_view()),
    path('categorias/', CategoriaList.as_view()),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
