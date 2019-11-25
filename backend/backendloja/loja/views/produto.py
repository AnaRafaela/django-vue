from rest_framework import generics, permissions

from loja.models import Produto
from loja.serializers import ProdutoSerializer

class ProdutoList(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = ()

