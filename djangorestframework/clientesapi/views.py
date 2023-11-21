from rest_framework import generics
from .models import Clientes
from .serializers import ClientesSerializer


class Clientes_Listar_CriarView(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


class Clientes_Opcoes_Atualizar_DeletarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
