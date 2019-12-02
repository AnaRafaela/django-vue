from rest_framework import generics

from loja.models import Categoria
from loja.serializers import CategoriaSerializer

class CategoriaList(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = ()

class CategoriaGet(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = ()