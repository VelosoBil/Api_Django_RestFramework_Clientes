from django.urls import path
from .views import Clientes_Listar_CriarView, Clientes_Opcoes_Atualizar_DeletarView

urlpatterns = [
    path('clientes/', Clientes_Listar_CriarView.as_view(), name='clientes-Lista-Novo'),
    path('clientes/<int:pk>/', Clientes_Opcoes_Atualizar_DeletarView.as_view(), name='clientes-opcoes-atualizar-deletar'),
]