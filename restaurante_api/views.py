#As views recebem a requisição do usuário (GET, POST, PUT, DELETE), acessam o banco via models e processam a lógica necessária. Depois, elas usam os serializers para transformar os dados e devolvem a resposta em JSON.




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import (
    Fornecedor,
    Ingrediente,
    Compra,
    Categoria,
    Produto,
    ProdutoIngrediente,
    Funcionario,
    Mesa,
    Cliente,
    Pedido,
    Pagamento,
    ItemPedido
)


from .serializers import (
    FornecedorSerializer,
    IngredienteSerializer,
    CompraSerializer,
    CategoriaSerializer,
    ProdutoSerializer,
    ProdutoIngredienteSerializer,
    FuncionarioSerializer,
    MesaSerializer,
    ClienteSerializer,
    PedidoSerializer,
    PagamentoSerializer,
    ItemPedidoSerializer
)




#FORNECEDOR
@api_view(['GET', 'POST']) #listar todos os fornecedores
def fornecedor_lista(request):
    if request.method == 'GET':
        fornecedor = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedor, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def listar_atualizar_deletar_fornecedor(request, id):
    try:
        fornecedor = Fornecedor.objects.get(pk=id)
    except Fornecedor.DoesNotExist:
        return Response({"Mensagem": "Fornecedor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = FornecedorSerializer(fornecedor, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Fornecedor atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = FornecedorSerializer(fornecedor, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Fornecedor atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response({"Mensagem": "fornecedor deletado com sucesso"}) #Remover informação


   
#INGREDIENTE
@api_view(['GET', 'POST'])
def ingrediente_lista(request):
    if request.method == 'GET': #listar todos os ingredientes
        ingrediente = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingrediente, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET' ,'PUT' ,'PATCH' ,'DELETE'])
def listar_atualizar_deletar_ingrediente(request, id):
    try:
        ingrediente = Ingrediente.objects.get(pk=id)
    except Ingrediente.DoesNotExist:
        return Response({"Mensagem": "Ingrediente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = IngredienteSerializer(ingrediente, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Ingrediente atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = IngredienteSerializer(ingrediente, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Ingrediente atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response({"Mensagem": "Ingrediente deletado com sucesso"}) #Remover informação






#COMPRA
@api_view(['GET', 'POST'])
def compra_lista(request):
    if request.method == 'GET': #listar todos as compras
        compra = Compra.objects.all()
        serializer = CompraSerializer(compra, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET' ,'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_compra(request, id):
    try:
        compra = Compra.objects.get(pk=id)
    except Compra.DoesNotExist:
        return Response({"Mensagem": "Compra não encontrada"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = CompraSerializer(compra)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = CompraSerializer(compra, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Compra atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = CompraSerializer(compra, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Compra atualizado com sucesso!"})
        return Response({"Mensagem": "Compra inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        compra.delete()
        return Response({"Mensagem": "Compra deletado com sucesso"}) #Remover informação


#CATEGORIA
@api_view(['GET', 'POST'])
def categoria_lista(request):
    if request.method == 'GET':  # Listar todas as categorias
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Criar nova categoria
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar, atualizar ou deletar uma categoria específica
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        return Response({"Mensagem": "Categoria não encontrada"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)  # Detalhes específicos
   
    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)  # Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Categoria atualizada com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = CategoriaSerializer(categoria, data=request.data, partial=True)  # Atualizar uma informação específica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Categoria atualizada com sucesso!"})
        return Response({"Mensagem": "Categoria inválida"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        categoria.delete()
        return Response({"Mensagem": "Categoria deletada com sucesso"})  # Remover informação



#PRODUTO
@api_view(['GET', 'POST'])
def produto_lista(request):
    if request.method == 'GET': #listar todos as produtos
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'PATCH' ,'DELETE'])
def listar_atualizar_deletar_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        return Response({"Mensagem": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Produto atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = ProdutoSerializer(produto, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Produto atualizado com sucesso!"})
        return Response({"Mensagem": "Produto inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        produto.delete()
        return Response({"Mensagem": "Produto deletado com sucesso"}) #Remover informação






#PRODUTOINGREDIENTE
@api_view(['GET', 'POST'])
def produtoIngrediente_lista(request):
    if request.method == 'GET': #listar todos as produtoingrediente
        produtoIngrediente = ProdutoIngrediente.objects.all()
        serializer =  ProdutoIngredienteSerializer(produtoIngrediente, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = ProdutoIngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_produtoIngrediente(request, id):
    try:
       produtoIngrediente = ProdutoIngrediente.objects.get(pk=id)
    except ProdutoIngrediente.DoesNotExist:
        return Response({"Mensagem": "ProdutoIngrediente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = ProdutoIngredienteSerializer(produtoIngrediente)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = ProdutoIngredienteSerializer(produtoIngrediente, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "produtoIngrediente atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = ProdutoIngredienteSerializer(produtoIngrediente, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "produtoIngrediente atualizado com sucesso!"})
        return Response({"Mensagem": "produtoIngrediente inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        produtoIngrediente.delete()
        return Response({"Mensagem": "produtoIngrediente deletado com sucesso"})




#FUNCIONARIO
@api_view(['GET', 'POST'])
def funcionario_lista(request):
    if request.method == 'GET': #listar todos as Funcionario
        funcionario = Funcionario.objects.all()
        serializer =  FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_funcionario(request, id):
    try:
       funcionario = Funcionario.objects.get(pk=id)
    except Funcionario.DoesNotExist:
        return Response({"Mensagem": "Funcionario não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = FuncionarioSerializer(funcionario, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Funcionario atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = FuncionarioSerializer(funcionario, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Funcionario atualizado com sucesso!"})
        return Response({"Mensagem": "Funcionario inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        funcionario.delete()
        return Response({"Mensagem": "Funcionario deletado com sucesso"})




#MESA
@api_view(['GET', 'POST'])
def mesa_lista(request):
    if request.method == 'GET': #listar todos as Mesa
        mesa = Mesa.objects.all()
        serializer = MesaSerializer(mesa, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = MesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_mesa(request, id):
    try:
       mesa = Mesa.objects.get(pk=id)
    except Mesa.DoesNotExist:
        return Response({"Mensagem": "Mesa não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = MesaSerializer(mesa)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = MesaSerializer(mesa, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Mesa atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = MesaSerializer(mesa, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Mesa atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        mesa.delete()
        return Response({"Mensagem": "Mesa deletado com sucesso"})




#CLIENTE
@api_view(['GET', 'POST'])
def cliente_lista(request):
    if request.method == 'GET': #listar todos as cliente
        cliente= Cliente.objects.all()
        serializer =  ClienteSerializer(cliente, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_cliente(request, id):
    try:
       cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        return Response({"Mensagem": "Cliente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Cliente atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = ClienteSerializer(cliente, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Cliente atualizado com sucesso!"})
        return Response({"Mensagem": "formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        cliente.delete()
        return Response({"Mensagem": "Cliente deletado com sucesso"})






#PEDIDO
@api_view(['GET', 'POST'])
def pedido_lista(request):
    if request.method == 'GET': #listar todos os pedido
        pedido = Pedido.objects.all()
        serializer = PedidoSerializer(pedido, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_pedido(request, id):
    try:
       pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        return Response({"Mensagem": "Pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = PedidoSerializer(pedido, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pedido atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = PedidoSerializer(pedido, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pedido atualizado com sucesso!"})
        return Response({"Mensagem": "formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        pedido.delete()
        return Response({"Mensagem": "Pedido deletado com sucesso"})


#PAGEMENTO
@api_view(['GET', 'POST'])
def pagamento_lista(request):
    if request.method == 'GET': #listar todos os pagamento
        pagamento = Pagamento.objects.all()
        serializer = PagamentoSerializer(pagamento, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = PagamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_pagamento(request, id):
    try:
       pagamento = Pagamento.objects.get(pk=id)
    except Pagamento.DoesNotExist:
        return Response({"Mensagem": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = PagamentoSerializer(pagamento)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = PagamentoSerializer(pagamento, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pagamento atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = PagamentoSerializer(pagamento, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pagamento atualizado com sucesso!"})
        return Response({"Mensagem": "formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        pagamento.delete()
        return Response({"Mensagem": "Pagamento deletado com sucesso"})




#ITEMPEDIDO
@api_view(['GET', 'POST'])
def itemPedido_lista(request):
    if request.method == 'GET': #listar todos os intenPedido
        itemPedido = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(itemPedido, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = ItemPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT' ,'PATCH', 'DELETE'])
def listar_atualizar_deletar_itemPedido(request, id):
    try:
       itemPedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        return Response({"Mensagem": "itemPedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = ItemPedidoSerializer(itemPedido)
        return Response(serializer.data) #Detalhes  específico
   
    elif request.method == 'PUT':
        serializer = ItemPedidoSerializer(itemPedido, data=request.data) #Atualizar informações
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "itemPedido atualizado com sucesso!"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PATCH':
        serializer = ItemPedidoSerializer(itemPedido, data=request.data, partial=True) #atualizar uma informações especifica
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "ItemPedido atualizado com sucesso!"})
        return Response({"Mensagem": "formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        itemPedido.delete()
        return Response({"Mensagem": "ItemPedido deletado com sucesso"})

