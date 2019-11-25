from rest_framework import generics, permissions

from loja.models import Carrinho
from loja.serializers import CarrinhoSerializer


class CarrinhoList(generics.ListAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = ()


class CarrinhoDestroy(generics.DestroyAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CarrinhoUpdate(generics.UpdateAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CarrinhoCreate(generics.CreateAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = ()


class CarrinhoGet(generics.RetrieveAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = ()
