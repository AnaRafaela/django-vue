from rest_framework import generics, permissions

from loja.models import Produto
from loja.serializers import ProdutoSerializer

class ProdutoList(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = ()

class ProdutoGet(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = ()
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        categoria = self.kwargs['categoria']
        return Produto.objects.filter(categoria=categoria)

class ProdutoDetailGet(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = ()

