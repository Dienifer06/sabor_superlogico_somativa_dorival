#O urls.py define quais endereços (rotas) a API terá e para qual view cada rota deve enviar a requisição. Ele funciona como um “mapa” que conecta a URL certa com a função certa no backend.
from django.urls import path
from .views import (
    fornecedor_lista,
    listar_atualizar_deletar_fornecedor,


    ingrediente_lista,
    listar_atualizar_deletar_ingrediente,


    produto_lista,
    listar_atualizar_deletar_produto,


    compra_lista,
    listar_atualizar_deletar_compra,


    funcionario_lista,
    listar_atualizar_deletar_funcionario,


    mesa_lista,
    listar_atualizar_deletar_mesa,


    cliente_lista,
    listar_atualizar_deletar_cliente,


    pedido_lista,
    listar_atualizar_deletar_pedido,


    pagamento_lista,
    listar_atualizar_deletar_pagamento,


    itemPedido_lista,
    listar_atualizar_deletar_itemPedido,


    produtoIngrediente_lista,
    listar_atualizar_deletar_produtoIngrediente,

    categoria_lista,
    listar_atualizar_deletar_categoria
)




urlpatterns = [
    path('fornecedor/', fornecedor_lista, name='fornecedor_lista'),
    path('fornecedor/<int:id>/',listar_atualizar_deletar_fornecedor, name='listar_atualizar_deletar_fornecedor'),


    path('ingrediente/', ingrediente_lista, name='ingrediente_lista'),
    path('ingrediente/<int:id>/',listar_atualizar_deletar_ingrediente, name='listar_atualizar_deletar_ingrediente'),


    path('produto/', produto_lista, name='produto_lista'),
    path('produto/<int:id>/',listar_atualizar_deletar_produto, name='listar_atualizar_deletar_produto'),


    path('compra/', compra_lista ,name='compra_lista'),
    path('compra/<int:id>/',listar_atualizar_deletar_compra, name='listar_atualizar_deletar_compra'),


    path('produtoIngrediente/',produtoIngrediente_lista, name='produtoIngrediente_lista'),
    path('produtoIngrediente/<int:id>/',listar_atualizar_deletar_produtoIngrediente, name='listar_atualizar_deletar_produtoIngrediente'),


    path('funcionario/', funcionario_lista, name='funcionario_lista'),
    path('funcionario/<int:id>/',listar_atualizar_deletar_funcionario, name='listar_atualizar_deletar_funcionario'),


    path('mesa/', mesa_lista, name='mesa_lista'),
    path('mesa/<int:id>/',listar_atualizar_deletar_mesa, name='listar_atualizar_deletar_mesa'),


    path('cliente/',cliente_lista ,name='cliente_lista'),
    path('cliente/<int:id>/',listar_atualizar_deletar_cliente, name='listar_atualizar_deletar_cliente'),


    path('pedido/',pedido_lista ,name='pedido_lista'),
    path('pedido/<int:id>/',listar_atualizar_deletar_pedido, name='listar_atualizar_deletar_pedido'),


    path('pagamento/',pagamento_lista, name='pagamento_lista'),
    path('pagamento/<int:id>/',listar_atualizar_deletar_pagamento, name='listar_atualizar_deletar_pagamento'),


    path('itemPedido/', itemPedido_lista ,name='itemPedido_lista'),
    path('itemPedido/<int:id>/',listar_atualizar_deletar_itemPedido, name='listar_atualizar_deletar_itemPedido'),

    path('categoria/', categoria_lista, name='categoria_lista'),
    path('categoria/<int:id>/', listar_atualizar_deletar_categoria, name='listar_atualizar_deletar_categoria'),


]
























   






























 





















