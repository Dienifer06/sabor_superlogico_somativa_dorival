#Em Django, um model é uma classe Python que representa uma tabela do banco de dados.Cada atributo dentro do model representa uma coluna da tabela.E cada instância do model representa uma linha (um registro).
from django.db import models


class Fornecedor(models.Model):
  nome = models.CharField(max_length=100)
  contato = models.CharField(max_length=100)
  telefone = models.CharField(max_length=20)
  email = models.CharField(max_length=100)


  def __str__(self):
            return self.nome




class Ingrediente(models.Model):
  nome = models.CharField(max_length=100)
  quantidade_ingrediente = models.DecimalField(max_digits=10, decimal_places=2)
  unidade_medida = models.CharField(max_length=100)


  def __str__(self):
        return self.nome




class Compra(models.Model):
  quantidade = models.DecimalField(max_digits=10, decimal_places=2)
  data_compra = models.DateTimeField()
  valor_total = models.DecimalField(max_digits=10, decimal_places=2)
  fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
  ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
 


class Categoria(models.Model):
  nome = models.CharField(max_length=50)
  descricao = models.TextField()


  def __str__(self):
        return self.nome


class Produto(models.Model):
  nome = models.CharField(max_length=100)
  descricao = models.TextField()
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  estoque = models.PositiveSmallIntegerField()


  def __str__(self):
        return self.nome


class ProdutoIngrediente(models.Model):
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
  quantidade_usada = models.DecimalField(max_digits=10, decimal_places=2)




class Funcionario(models.Model):
  nome = models.CharField(max_length=100)
  cargo = models.CharField(max_length=50)
  email = models.CharField(max_length=100)
  telefone = models.CharField(max_length=20)
  senha = models.CharField(max_length=100)


  def __str__(self):
        return self.nome




class Mesa(models.Model):
  TIPO_MESA_CHOICES = [
    ('L', 'Livre'),
    ('O', 'Ocupada'),
    ('R', 'Reservada'),
]
  numero = models.PositiveIntegerField()
  capacidade = models.PositiveIntegerField()
  status = models.CharField(max_length=1,choices=TIPO_MESA_CHOICES)
 




class Cliente(models.Model):
  TIPO_CLIENTE_CHOICES = [
    ('P', 'Premium'),
    ('R', 'Regular'),
    ('I', 'Intermediario'),
]
  nome = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  telefone = models.CharField(max_length=20)
  endereco = models.CharField(max_length=255)
  tipo_cliente = models.CharField(max_length=1,choices= TIPO_CLIENTE_CHOICES)
  def __str__(self):
        return self.nome




class Pedido(models.Model):


    TIPO_PEDIDO_CHOICES = [
    ('P', 'Pronto'),
    ('F', 'Fazendo'),
    ('E', 'Espera'),
]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    date_hora = models.DateTimeField()
    observacao = models.TextField()
    status = models.CharField(max_length=7,choices=TIPO_PEDIDO_CHOICES)
   


class Pagamento(models.Model):
    TIPO_PAGAMENTO_CHOICES = [
    ('C', 'Credito'),
    ('D', 'Debito'),
    ('P', 'Pix'),
]
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()
    tipo_pagamento = models.CharField(max_length=1,choices=TIPO_PAGAMENTO_CHOICES)


   




class ItemPedido(models.Model):
  pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.PositiveIntegerField()
  preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
































 





