from .models import Fornecedor, Ingrediente,Compra,Produto,ProdutoIngrediente,Funcionario,Mesa,Cliente,Pedido,Pagamento,ItemPedido,Categoria
from rest_framework import serializers


#Um serializer pega um objeto do Django (ex: Cliente) e transforma em JSON
class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera




class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera



class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera




class ProdutoIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoIngrediente
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Cliente
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Pedido
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__' #pega tudo
        read_only_fields = ['id']#não altera














